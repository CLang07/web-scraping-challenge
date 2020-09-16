# dependancies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

def scrape():
    # Initialize website
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    # pause to let page load
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # Scrape website
    results = soup.find_all("div", class_="list_text")
    title_list=[]
    paragraph_list=[]
    #Finds titles and paragraphs of each news article
    for result in results:
        title = result.find("div", class_="content_title")
        paragraph = result.find("div",class_="article_teaser_body")
        # tests for errors
        if title:
            title_list.append(title.text)     
        else:
            title_list.append("")
        
        if paragraph:
            paragraph_list.append(paragraph.text)
        else:
            paragraph_list.append("")
    # Creates dictionary of most recent news title and paragraph
    news = {
        "titles":title_list[0],
        "paragraphs":paragraph_list[0]
    }
    # Initialize website and scrape
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")  

    # find current Featured Mars Image
    featured_image = soup.find("footer").find("a")['data-fancybox-href']
    featured_image_url = f"https://www.jpl.nasa.gov"+featured_image

    # scrapes mars facts table
    url = "https://space-facts.com/mars/"
    tables = pd.read_html(url)
    mars_df = tables[0]
    mars_df.columns=['Attribute','Value']
    mars_df = mars_df.set_index('Attribute')
    mars_json = json.loads(mars_df.T.to_json()).values()
    mars_dict = mars_df.to_dict()
    
    # Initialize website and scrape    
    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    #finds links to all hemisphere webpages 
    results = soup.find_all("div",class_='item')
    link_list=[]
    for result in results:
        link = result.find("a")['href']
        link_list.append(link)

    # loops through each hemisphere page and pulls title and image_url
    url = 'https://astrogeology.usgs.gov'
    title_list=[]
    image_list=[]
    for link in link_list:
        browser.visit(url+link)
        html = browser.html
        soup = BeautifulSoup(html, "html.parser")
        image_url = soup.find('div', class_='downloads').a['href']
        title = soup.find("h2",class_='title').text
        title_list.append(title)
        image_list.append(image_url)

    # creates dictionary in requested format
    mars_img_dict = [
    {'title' : title_list[0],'img_url' : image_list[0]},
    {'title' : title_list[1],'img_url' : image_list[1]},
    {'title' : title_list[2],'img_url' : image_list[2]},
    {'title' : title_list[3],'img_url' : image_list[3]},
    ]
    # Creates dictionary of scraped data
    mars = {
        'news':news,
        'featured_image_url':featured_image_url,
        'mars_dict':mars_dict,
        'mars_img_dic':mars_img_dict
    }
    return mars