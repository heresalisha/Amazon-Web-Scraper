# Amazon-Web-Scraper

## Abstract :

In this documentation a web scraper is implemented in python which extracts relevant data from an e-commerce website specified i.e. amazon . The details are then stored in SQLite database format. A Virtual environment is used to scrape the details of the products available on amazon
 
## Introduction : 

Web scraping is the process of gathering information from the Internet.A web scraping tool is a software program that’s designed specifically to extract (or ‘scrape’) relevant information from websites. You’ll almost certainly be using some kind of scrape tool whenever you are collecting data from web pages programmatically..
We are using one of the popular shopping sites https://www.amazon.com/ for this project. Amazon is the world’s most trusted recommendation resource for quality shopping. 
The scraper requests the url and fetches the data one by one according to the specified rules as the individual data is fetched it simultaneously keeps adding it to the view section.  
### Methodology : 
Steps to extract the data using web scraper

1.Find the URL that you want to scrape.

2.Inspecting the Page.

3.Find the data you want to extract.

4.Write the code.

5.Run the code and extract the data.

6.Store the data in the required format.


## Requirements : 

Make sure that browsers such as chrome, IE or other have been installed in the environment. 

Download and install python 

Download a suitable IDE for this specific project visual studio code. 

Make sure pip is properly configured. 

Pip : Python package management tool used for searching, downloading, installing and uninstalling python packages. 

Install the required python packages. 

beautifulsoup4 4.10.0

Flask 2.0.2

requests 2.26.0

ECOMMERCE-WEB SCRAPER : Root directory of the project 

env : Virtual environment of the project 

app.py : Main file containing the main script.

static : contains scripts ,styles and images.

templates :  contains all the views of the application.

Scraper.py : code to implement scraper in the application.

products.db : product details will be stored in SQLite format 

Requirements.txt : descriptor for all the external libraries and dependencies used in our application. 
 
 
# Conclusion : 

The above project demonstrates just one use case of the web scraper that is to scrap a product details site for data on amazon. The scrapers perfectly fulfill the purpose it was intended to do. 

My project is just another implementation of a general purpose web scraper(One of the mechanisms for retrieving data from the web). This program can be implemented in multiple ways and for various different purposes. 






