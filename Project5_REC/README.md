# **Metis Project 5 - Summer 2020**

**Author**

Frederick Lam

**About**

This project focuses on creating a Anime Collaborative Filtering (CF) Recommender using the Surprise python package. The data has been requested from an unofficial open source API,  <a href="https://jikan.moe/" target="_blank">Jikan</a>, for MyAnimeList.net. In addition to creating the recommender, it also includes an interactive streamlit app that's been deployed on heroku <a href="https://p5-anime-app.herokuapp.com/" target="_blank">here</a>.

**Files**

- Code
  - MAL_API.ipynb
    - This notebook contains the code to request from the Jikan API and pulls information for each anime review and general information about the anime (MPAA rating, genres)
    - Keep in mind that this notebook does take a while to run due to MyAnimeList's HTTP inconsistency
    - You'll need to export the rate_df and det_df dataframes into .csv in order to get the MAL_REC notebook to work
  - MAL_REC.ipynb
    - This notebook covers the cleaning and modeling of the CF recommender, as well as some test runs for the streamlit app's code
    - You'll need to pickle the rate_df/score_df and det_df dataframes in order to get the streamlit python file to work
- Streamlit
  - p5_app.py
    - This python file includes the code to run the streamlit app, you'll notice that most of the code is shared with MAL_REC.ipynb
    - example.pkl can be ommitted from the code as that was just to display a sample of the .csv input for the app

**Required Packages**

<a href="https://pypi.org/project/scikit-surprise/" target="_blank">Surprise</a>

<a href="https://jikan.moe/" target="_blank">Jikan</a>

<a href="https://docs.streamlit.io/en/stable/" target="_blank">Streamlit</a>

**Tools**

- Python: pandas, numpy, time
- Surprise: SVD, GridSearchCV
- Streamlit				

**Techniques**

- Collaborative Filtering Recommender system