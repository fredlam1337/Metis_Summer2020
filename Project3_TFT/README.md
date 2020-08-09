# **Metis Project 3 - Summer 2020**

**Author**

Frederick Lam

**About**

This project focuses on using supervised data to create a classifier. In this context, the goal is to predict a win or loss using kaggle data on the popular video game, Teamfight Tactics, using a machine learning algorithm. The data comes from part one of the game's set 3 update, Galaxies.

The size of the tested dataset contains 800,000 observations and 106 features. Features include the total game duration, player level, and item and star values for each available champion.

This project also showcases an interactive flask web app that was created to emphasize the practicality of the finalized model.

**Files**

- Code
  - TFT_CleanCSV.ipynb
    - Import the datasets downloaded from https://www.kaggle.com/gyejr95/tft-match-data?select=TFT_Platinum_MatchData.csv and use this notebook to clean and engineer the datasets into exported .csv files
  - TFT_SQL_ModelTesting.ipynb
    - This notebook uses SQLAlchemy that takes the uploaded datasets from AWS into python. Please be aware, it does take quite a while to read the data from AWS so the model reads an exported .csv that was created from the joined datasets.
- TFT_Flask_app (please place into this folder my_pickled_model.p from TFT_SQL_ModelTesting.ipynb to make this work)
  - main.py
  - make_prediction.py
  - templates
    - index.html (keep in mind, this file is really messy and could've been improved with extended knowledge of html and js)
- README.md

**Tools**

- AWS, Postgresql

- Python: Pandas, Numpy, Matplotlib, Seaborn, SQLAlchemy, AST
- Scikit-Learn:
  - KNN, Logistic Regression, Decision Tree Classifier, Random Forest Classifier, GaussianNB, svm.LinearSVC
- Flask, HTML, CSS, JavaScript					

**Testing**

- EDA
- Machine Learning Classification