# **Metis Project 2 - Summer 2020**

**Author**

Frederick Lam

**About**

MAL (myanimelist.net) is a popular site for information about anime shows and serializations. My goal is to predict the weighted score of a show using their film rating, type of show, status, number of registered users who scored and favorited the show, episode count, number of registered clubs, and number of forum posts and replies. 

The primary goal for this project is to incorporate regression using supervised variables. The focused ones in this project as linear, ridge, and LASSO.

**Files**

- Code
  - MAL.ipynb
  - MALFunc.py
  - MALData.ipynb
  - p2.ipynb
- README.md

**File Workflow** (from top to bottom)

MAL.ipynb = notebook where I tested all my code for web scraping, it's quite messy but includes all my trial and error

MALFunc.py = python file that includes all the finalized code from MAL.ipynb set up into multiple functions for import

MALData.ipynb = notebook that uses the functions from MALFunc.py to scrape the data off myanimelist and save it into a csv named ani_data.csv

- **Disclaimer**: you will need to set up a seperate csv or web scrape function that has two columns, one with the show link and the other with the show number, to get MALData to work. Web scraping it is VERY DIFFICULT because many shows have missing values so I recommend a csv (mine is named anime_links.csv in the notebook)

p2.ipynb = notebook that reads in ani_data.csv and where I cleaned, performed EDA, and did my testing and modeling

**Data**

https://myanimelist.net/

**Tools**

- Python
- Pandas
- Numpy
- BeautifulSoup
- Selenium
- Matplotlib
- Seaborn
- Scikit-Learn:
  - Linear regression
  - Ridge regression
  - LASSO regression				

**Analysis**

- Exploratory Data Analysis
- Machine Learning Regression Analysis