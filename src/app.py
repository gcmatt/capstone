from flask import Flask, render_template, request
from wtforms import Form, StringField, validators
from src.models.search import Search

app = Flask(__name__)
app.secret_key = "ctis_capstone"

class SearchForm(Form):
    title = StringField('title', [validators.InputRequired()])

@app.route('/')
def home_page():
    return render_template('home.html')


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


