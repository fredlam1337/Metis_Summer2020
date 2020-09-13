#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 11:47:41 2020

@author: dragoslol
"""

import streamlit as st
import pandas as pd
import numpy as np

from surprise import Dataset, Reader, SVD

from collections import defaultdict
from ast import literal_eval

st.title('MAL Anime CF Recommender')

st.header('**Instructions:**')
st.subheader('Choose categories from either or both genre and rating to filter out your \
            recommendations')

st.markdown('**OPTIONAL**: To get recommendations based off your watch history, \
            upload a .csv in this specific format (max 200MB):')

example_df = pd.read_pickle('example.pkl')
st.table(example_df.head(3))

st.markdown('Anime titles must be taken straight from https://myanimelist.net/')
st.markdown('Make sure to paste the bolded titles on the site into your .csv for it to work')
st.markdown('Feel free to make up a username and scores can be either int (i.e. 1) or float (i.e. 1.0)')
st.markdown('**VERY IMPORTANT: YOU MUST HAVE AT LEAST 2 REVIEWS IN YOUR FILE**')

score_df = pd.read_pickle('score_df.pkl')
det_df = pd.read_pickle('det_df.pkl')

# user file
st.set_option('deprecation.showfileUploaderEncoding', False)
file = st.file_uploader("Upload file", type=["csv"])
 
if file:
    test_csv = pd.read_csv(file)
    test_csv['Score'] = test_csv['Score'].map(int)
    st.markdown('Your File')
    st.dataframe(test_csv.head(5))
    
    df_list = [score_df, test_csv]
    score_df = pd.concat(df_list)
else:
    pass

# get list of genres
g = []
for gn in det_df['Genres']:
    g.append(literal_eval(gn))

tg = []
for g_list in g:
    tg += g_list

g_select = sorted(list(set(tg)))

# get list of ratings
r = []

for rating in det_df['Rating']:
    r.append(rating)

r_select = sorted(list(set(r)))

selected_genre = st.multiselect('Genre(s)', g_select)
selected_rating = st.multiselect('Rating(s)', r_select)

st.markdown('**Recommendations:**')

# creates AnimeID for each anime
# score_df
grouped_name = score_df.groupby('Anime')

temp_df = grouped_name.count()
temp_df_idx = pd.DataFrame(temp_df.index)

temp_df_idx['AnimeID'] = temp_df_idx.index
dict_df=temp_df_idx[['AnimeID','Anime']]

desc_dict = dict_df.set_index('Anime').to_dict()
new_dict = desc_dict['AnimeID']

score_df['AnimeID'] = score_df['Anime'].map(new_dict)

# det_df
grouped_name = det_df.groupby('Anime')

temp_df = grouped_name.count()
temp_df_idx = pd.DataFrame(temp_df.index)

temp_df_idx['AnimeID'] = temp_df_idx.index
dict_df=temp_df_idx[['AnimeID','Anime']]

desc_dict = dict_df.set_index('Anime').to_dict()
new_dict = desc_dict['AnimeID']

det_df['AnimeID'] = det_df['Anime'].map(new_dict)

# create UserID for each user
grouped_user = score_df.groupby('User')

temp_df_user = grouped_user.count()
temp_df_user_idx = pd.DataFrame(temp_df_user.index)

temp_df_user_idx['UserID']=temp_df_user_idx.index
dict_df_user=temp_df_user_idx[['UserID','User']] 

desc_dict_user = dict_df_user.set_index('User').to_dict()
new_dict_user = desc_dict_user['UserID']

score_df['UserID'] = score_df['User'].map(new_dict_user)

# retrieve user's ID
if file:
    new_user = score_df['UserID'][score_df['User'] == test_csv['User'][0]][0]
else:
    new_user = None

# remove shows/users with low counts
min_anime_ratings = 2
min_user_ratings =  2

clean_ani_ratings = score_df.groupby('AnimeID').filter(lambda x: x['AnimeID'].count() >= min_anime_ratings)
test_df = clean_ani_ratings.groupby('UserID').filter(lambda x: x['UserID'].count() >= min_user_ratings)

# model
reader = Reader(rating_scale=(test_df['Score'].min(), test_df['Score'].max()))
data = Dataset.load_from_df(test_df[["UserID", "AnimeID", "Score"]], reader=reader)

trainset = data.build_full_trainset()
testset = trainset.build_anti_testset()

algo_SVD = SVD(n_factors = 5, random_state=4444)
algo_SVD.fit(trainset)

testset = trainset.build_anti_testset()

predictions = algo_SVD.test(testset)

# borrowed from https://www.jiristodulka.com/post/recsys_cf/ 
def get_top_n(predictions, userId, anime_df, ratings_df, n = 50):
    # map the predictions to each user
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))

    # sort the predictions for each user and retrieve the k highest ones
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key = lambda x: x[1], reverse = True)
        top_n[uid] = user_ratings[: n ]
    
    # returns how many movies the user has already rated
    user_data = ratings_df[ratings_df['UserID'] == (userId)]
    print('User {0} has already rated {1} shows/movies.'.format(userId, user_data.shape[0]))

    # DataFrame with predictions
    preds_df = pd.DataFrame([(id, pair[0],pair[1]) for id, row in top_n.items() for pair in row],
                        columns=['UserID' , 'AnimeID', 'PredScore'])
    
    # return top N recommended anime with (merged) titles and genres 
    pred_usr = preds_df[preds_df['UserID'] == (userId)].merge(anime_df, how = 'left', left_on = 'AnimeID', right_on = 'AnimeID')
            
    # return top N historically rated anime with (merged) titles and genres for holistic evaluation
    hist_usr = ratings_df[ratings_df['UserID'] == (userId) ].sort_values('Score', ascending = False).merge\
    (anime_df, how = 'left', left_on = 'AnimeID', right_on = 'AnimeID')
    
    return hist_usr, pred_usr

# return output
if new_user != None:
    hist_SVD, pred_SVD = get_top_n(predictions, anime_df = det_df, userId = new_user, ratings_df = test_df)
else:
    pred_SVD = det_df

test_in = []
test_in2 = []

for index, rating in enumerate(pred_SVD['Rating']):
    if rating in selected_rating:
        test_in.append(index)
        
for index, gn in enumerate(pred_SVD['Genres']):
    if all(x in literal_eval(gn) for x in selected_genre):
        test_in2.append(index)
            
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3

if test_in and test_in2:
    final_list = intersection(test_in, test_in2)
    
    for num in final_list[:10]:
        st.text(pred_SVD.iloc[num].Anime)
elif test_in:
    for num in test_in[:10]:
        st.text(pred_SVD.iloc[num].Anime)
elif test_in2:
    for num in test_in2[:10]:
        st.text(pred_SVD.iloc[num].Anime)

