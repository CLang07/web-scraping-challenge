# Web Scraping Homework - Mission to Mars

This progam is a web application that scrapes the mars.nasa.gov website for the news, featured image, facts, and hemisphere images.  The data is stored into MongoDB and displayed in an HTML page using flask.

Screen captures of the web page can be viewed in files HTML_Display_Page_1.png and HTML_Display_Page_2.png

Files:
scrape_mars.py scrapes all of the data from the mars website

mission_to_mars.ipynb is a jupyter notebook version of the scrape_mars.py file

template/index.html formats and visualizes the data

app.py runs scrape_mars.py and stores the data in MongoDB.  It then uses the index.html file to display the data on a web page

