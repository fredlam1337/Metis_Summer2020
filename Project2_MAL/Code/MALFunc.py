#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 14:37:21 2020

@author: dragoslol
"""
from bs4 import BeautifulSoup
import requests
import time, os
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def ani_details(link):
    """

    Scrapes off the detail page of a show on myanimelist.net using
    beautifulsoup
    
    Features: title, type, status, studio, source, genres, rating,
    score, scored by, and favorites
    
    EDIT: some features are commented out by default for testing purposes
    
    Returns a dictionary with values and corresponding headers/keys

    """
    base_url = 'https://myanimelist.net/anime/'
    url = base_url + link

    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "lxml")

    headers = ['title', 'type', 'status', 'source', 'rating', 'score', 'scored by', 'favorites']

    #title
    n_title = soup.find('span', itemprop='name')
    regex = re.compile(r"<br/?>", re.IGNORECASE)
    newtext = re.sub(regex, ': ', str(n_title))
    eng_title = BeautifulSoup(newtext, "lxml").text


    #type
    ani_type = soup.find('span', string='Type:').findNext('a').contents[0]
    
    #status
    status = soup.find('span', string='Status:')
    status_text = status.next_sibling
    ani_status = status_text.strip()

    #studio
    #studios = soup.find('span', string='Studios:').next_sibling
    #ani_studio = studios.next_sibling.text

    #source
    source = soup.find('span', string='Source:')
    source_text = source.next_sibling
    ani_source = source_text.strip()

    #genres
    #genre_li = []
    #genres = soup.find_all('span', itemprop = 'genre')
    #for genre in genres:
        #genre_li.append(genre.text)

    #rating
    rating = soup.find('span', string='Rating:')
    rating_text = rating.next_sibling
    rate_li = rating_text.strip().split()
    ani_rating = ''.join(rate_li[:1])

    #score
    score = soup.find('span', itemprop = 'ratingValue').text
    score = float(score)

    #score by count
    score_count = soup.find('span', itemprop = 'ratingCount').text
    score_count = int(score_count)

    #favorites
    favorites = soup.find('span', string='Favorites:')
    favorites_text = favorites.next_sibling
    favs = int(favorites_text.replace(',', ''))

    ani_dict = dict(zip(headers, [eng_title,
                                    ani_type,
                                    ani_status,
                                    ani_source, 
                                    ani_rating,
                                    score,
                                    score_count,
                                    favs]))
    return ani_dict

def get_episodes(link):
    """
    
    Scrapes off the episode page of a show on myanimelist.net using
    beautifulsoup
    
    Features: episode count
    
    If episode page doesn't exist, such as a movie, takes info from detail page
    
    Returns a dictionary with values and corresponding headers/keys

    """
    base_url = 'https://myanimelist.net/anime/'
    url = base_url + link + '/episode'
    response = requests.get(url)
    
    if response.status_code == 200:
        page = response.text
        soup = BeautifulSoup(page, "lxml")
    
        episodes = soup.find('span', class_ = 'di-ib pl4 fw-n fs10').text
        total_episodes = episodes.split('/')[0].strip('()')
        total_episodes = int(total_episodes)
    else:
        url = base_url + link
        response = requests.get(url)
        page = response.text
        soup = BeautifulSoup(page, "lxml")
        
        epi = soup.find('span', string='Episodes:')
        epi_text = epi.next_sibling
        total_episodes = epi_text.strip()
        total_episodes = int(total_episodes)
    
    headers = ['episodes']
    
    epi_dict = dict(zip(headers, [total_episodes]))
    
    return epi_dict

def get_characters(link):
    """
    
    Scrapes off the characters page of a show on myanimelist.net using
    beautifulsoup
    
    Features: character count
    
    Only scrapes the character section of the page, not including staff section
    
    Returns a dictionary with values and corresponding headers/keys
    
    EDIT: THIS CURRENTLY DOES NOT WORK AS INTENDED

    """
    base_url = 'https://myanimelist.net/anime/'
    url = base_url + link + '/characters'
        
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "lxml")
        
    headers = ['character count']
    
    #char count
    target = soup.find_all('h2')
    char = []
    
    for tag in target[3].next_siblings:
        a = tag.find('td', 'a', valign = 'top', class_ = ['borderClass bgColor1', 'borderClass bgColor2'], align = False)
        if a:
            char.append(a.find('a').text)
        else:
            pass
        if tag.name == "div":
            break
    
    char_count = len(char)
    char_dict = dict(zip(headers, [char_count]))
    
    return char_dict

def get_clubs(link):
    """
    
    Scrapes off the clubs page of a show on myanimelist.net using
    beautifulsoup
    
    Features: club count
    
    Returns a dictionary with values and corresponding headers/keys

    """
    base_url = 'https://myanimelist.net/anime/'
    url = base_url + link + '/clubs'
            
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, "lxml")
            
    headers = ['club count']
    
    club_li = []
    
    clubs = soup.find_all('div', class_ = 'borderClass')
    for club in range(len(clubs)):
        club_li.append(clubs[club].find('a').text)
    
    club_count = len(club_li)
    club_dict = dict(zip(headers, [club_count]))
    
    return club_dict

def get_reviews(link):
    """
    
    Scrapes off the reviews page of a show on myanimelist.net using
    beautifulsoup + selenium (chrome)
    
    Features: review count
    
    Iterates through the reviews 40 times, since that seems to be the max number
    for a show
    
    Returns a dictionary with values and corresponding headers/keys
    
    EDIT: THIS CURRENTLY DOES NOT WORK AS INTENDED

    """
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    base_url = 'https://myanimelist.net/anime/'
    url = base_url + link + '/reviews'
                
    headers = ['review count']

    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    total_review = []

    reviews = soup.find_all('span', id=re.compile("rhelp"))
    for review in reviews:
        total_review.append(review.text)
    
    if soup.find('a', text = 'More Reviews'):
        for i in range(1,40):
            next_button = driver.find_element_by_xpath(
                '//a[contains(text(), "More Reviews")]'
            )
            next_button.click()
    
            soup = BeautifulSoup(driver.page_source, 'html.parser')
    
            reviews = soup.find_all('span', id=re.compile("rhelp"))
            for review in reviews:
                total_review.append(review.text)
            
            time.sleep(2)
    
    driver.quit()
    total_rvs = len(total_review)
    
    review_dict = dict(zip(headers, [total_rvs]))
    
    return review_dict
    
def forum_posts(number):
    """
    
    Scrapes off the forum page of a show on myanimelist.net using
    beautifulsoup + selenium (chrome)
    
    Features: forum post count
    
    Calculates the total amount of posts by taking in the total number
    of forum pages, multiplying that, counting the first page, immediately
    go to last page to count, and taking the summed difference
    
    Returns a dictionary with values and corresponding headers/keys

    """
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    base_url = 'https://myanimelist.net/forum/?animeid='
    url = base_url + number
                
    headers = ['forum posts']

    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    pages = soup.find('span', class_ = 'di-ib').text
    total_pages = pages.split(' ')[1]
    
    total_pst = int(total_pages.strip('()'))
    total_pst = total_pst * 50
    
    post_li = []
    
    forum_posts = soup.find_all('td', class_ = 'forum_boardrow1')

    i = 0
    for j in range(len(forum_posts)):
        b = forum_posts[i].find_all('a', recursive = False)
        post_li.append(b[0].text)
        i += 2
        if i >= len(forum_posts):
            break
    
    post_count = len(post_li)
    
    if soup.find('a', text = 'Last »'):
        next_button = driver.find_element_by_xpath(
            '//a[contains(text(), "Last »")]'
        )
        next_button.click()
    
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    
        forum_posts = soup.find_all('td', class_ = 'forum_boardrow1')
    
        i = 0
        for j in range(len(forum_posts)):
            b = forum_posts[i].find_all('a', recursive = False)
            post_li.append(b[0].text)
            i += 2
            if i >= len(forum_posts):
                break
                
        #pages = soup.find('span', class_ = 'di-ib').text
        #total_pages = pages.split(' ')[1]
        total_pages = int(total_pages.strip('()')) - 2
        total_posts = total_pages * 50
        total_posts += len(post_li)
        
        post_count = total_posts
    
    elif soup.find('a', text = '3') and total_pst == 150:
        next_button = driver.find_element_by_xpath(
            '//a[contains(@href, "show=100")]'
        )
        next_button.click()
    
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    
        forum_posts = soup.find_all('td', class_ = 'forum_boardrow1')
    
        i = 0
        for j in range(len(forum_posts)):
            b = forum_posts[i].find_all('a', recursive = False)
            post_li.append(b[0].text)
            i += 2
            if i >= len(forum_posts):
                break
                
        #pages = soup.find('span', class_ = 'di-ib').text
        #total_pages = pages.split(' ')[1]
        total_pages = int(total_pages.strip('()')) - 2
        total_posts = total_pages * 50
        total_posts += len(post_li)
        
        post_count = total_posts

    elif soup.find('a', text = '2') and total_pst == 100:
        next_button = driver.find_element_by_xpath(
            '//a[contains(@href, "show=50")]'
        )
        next_button.click()
    
        soup = BeautifulSoup(driver.page_source, 'html.parser')
    
        forum_posts = soup.find_all('td', class_ = 'forum_boardrow1')
        # b = forum_posts[4].find_all('a', recursive = False)
    
        i = 0
        for j in range(len(forum_posts)):
            b = forum_posts[i].find_all('a', recursive = False)
            post_li.append(b[0].text)
            i += 2
            if i >= len(forum_posts):
                break
                
        #pages = soup.find('span', class_ = 'di-ib').text
        #total_pages = pages.split(' ')[1]
        total_pages = int(total_pages.strip('()')) - 1
        total_posts = total_pages * 50
        total_posts += len(post_li)
        
        post_count = total_posts
    
    post_count_dict = dict(zip(headers, [post_count]))
    
    driver.quit()
    
    return post_count_dict

def forum_replies(number):
    """
    
    Scrapes off the forum page of a show on myanimelist.net using
    beautifulsoup + selenium (chrome)
    
    Features: total forum replies
    
    Iterates until last page of forum posts
    
    Returns a dictionary with values and corresponding headers/keys

    """
    chromedriver = "/Applications/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    
    base_url = 'https://myanimelist.net/forum/?animeid='
    url = base_url + number
                
    headers = ['forum replies']

    driver = webdriver.Chrome(chromedriver)
    driver.get(url)
    
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    fr_li = []
    forum_replies = soup.find_all('td', class_ = 'forum_boardrow2', align = 'center', width = '75')

    for j in range(len(forum_replies)):
        fr_li.append(forum_replies[j].text)

    pages = soup.find('span', class_ = 'di-ib').text
    total_pages = pages.split(' ')[1]
    total_pages = int(total_pages.strip('()'))

    if soup.find('a', text = '»'):
        for page in range(total_pages - 1):
            next_button = driver.find_element_by_xpath(
                '//a[contains(text(), "»")]'
            )
            next_button.click()
    
            soup = BeautifulSoup(driver.page_source, 'html.parser')
    
            for j in range(len(forum_replies)):
                fr_li.append(forum_replies[j].text)
            
            time.sleep(2)

    sum_rlp = 0
    for i in fr_li:
        sum_rlp += int(i.replace(',',''))
    
    post_replies_dict = dict(zip(headers, [sum_rlp]))
    
    driver.quit()
    
    return post_replies_dict
