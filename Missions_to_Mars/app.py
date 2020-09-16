#  dependancies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
import pymongo

app = Flask(__name__)


conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_app

# Drops collection if available to remove duplicates
db.mars_app.drop()

@app.route("/")
def index():
    mars_data = db.mars_data.find_one()
    return render_template("index.html", mars_data=mars_data)

# @app.route("/scrape")
@app.route("/scrape")
def scrape():
    mars_data = scrape_mars.scrape()
    db.mars_data.update({}, mars_data, upsert=True)  
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)