# **Metis Project 4 - Summer 2020**

**Author**

Frederick Lam

**About**

This project focuses on performing NLP on unsupervised data. The topic of choice is using topic modeling on blog posts submitted by FGLI students about COVID-19 shared by <a href="https://risefirst.org/covid-19-blog?offset=1588041540856&reversePaginate=true">RiseFirst</a>.

**Files**

- Code
  - COVID_Scrape.ipynb
    - This notebook web scrapes the data using beautifulsoup and selenium, then outputs the data into covid_fgli.csv, which will be read in the COVID_TM notebook
  - COVID_TM.ipynb
    - This notebook covers the text preprocessing and topic modeling code performed on the data, along with some data visualization using matplotlib
- README.md

**Tools**

- Python: Pandas, Matplotlib, BeautifulSoup, Selenium
- NLTK:
  - WordTokenizer, MWETokenizer, WordNetLemmetizer
- Scikit-Learn:
  - CountVectorizer, NMF					

**Techniques**

- EDA
- NLP