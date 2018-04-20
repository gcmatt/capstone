import requests
from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
from src.models.search import Search, tmdb_key

#creates a flask app
app = Flask(__name__)
app.secret_key = "ctis_capstone"

#search form class
class SearchForm(Form):
    title = StringField('title', [validators.InputRequired()])


#the route for the sites home page
@app.route('/')
def home_page():
    return render_template('home.html')


#this route uses the input from the search form calls methods to pull data from the apis
#this data is then sent to the html template where most of the manipulation is done
@app.route('/search', methods=["POST"])
def search():
    form = SearchForm(request.form)
    if form.validate() is True:
        title = request.form['title']
        info = Search.tmdb_info(title)
        if not info:
            return render_template('noresults.html', title=title)
        else:
            nyt_info = Search.nytinfo(title)
            return render_template('search.html', title=title, info=info, nyt_info=nyt_info)
    else:
        print('3')
        return render_template('home.html')

#a route to the info page this is just a static page with text that is returned
@app.route('/info')
def info():
    return render_template('info.html')
