# -*- coding: utf-8 -*-
import pandas as pd
from pandas import json_normalize
import json
import sqlite3
from flask import Flask, render_template
import matplotlib.pyplot as plt

from app import app

# Open JSON data
with open("database.json") as f:
    data = json.load(f)

df = pd.json_normalize(data.values())
Table1 = df[['steam_appid', 'name', 'required_age', 'is_free', 'review_score', 'total_reviews']]

#dataframe to sql
import sqlite3
conn = sqlite3.connect('steam_database.dB')
c = conn.cursor()

#Create table
c.execute('CREATE TABLE IF NOT EXISTS Table1 (steam_appid number, name text, required_age numeric, is_free number, review_score number, total_reviews number)')
conn.commit()

#populate Table
Table1.to_sql('Table1', conn, if_exists='replace', index = False)

#query
c.execute("""SELECT * FROM Table1 WHERE review_score >= 8 AND required_age > 15 AND total_reviews >=1000""")
result = []
for row in c.fetchall():
    result.append(row)
Result =pd.DataFrame(result, columns=['steam_appid', 'name', 'required_age', 'is_free', 'review_score', 'total_reviews'])


@app.route('/')
@app.route('/index')
def index():

    # Open JSON data
    with open("database.json") as f:
        data = json.load(f)
    
    df = pd.json_normalize(data.values(), max_level=2)
    Data= df['name'][0]
    return render_template('index.html', data = Data, name = ' The mission of this project is to visualize the Steam dataset and deploy an app to answer the ultimate question: Is it worth investing more time into video games?', url = 'static/my_plot.png')


# =============================================================================
# @app.route('/Q')
# def Q():
#     Data = Result.to_html('Result.html')
#     #return Result
#     return render_template('Query.html')#Result.to_html(header="true", table_id="table")
# =============================================================================


@app.route('/v')
def visuals():
    import seaborn as sns
    sns.scatterplot(data=Result, x='required_age', y = 'total_reviews')
    plt.savefig('./app/static/my_plot.png')
    return render_template('Visuals.html', description = 'Sold units by month', name = 'Visuals', description1 = 'Top 10 games by sold items', description2 = 'Top 10 genres', url = 'static/Sold_units_by_month.png', url1 = 'static/Top_10_by_sold_units.png', url2 = 'static/Top_10_genres.png')

@app.route('/Q')
def query():
    return render_template("Query.html", data=Result.to_html(), name='Query', description = 'Query Table showing games where review_score >= 8, required_age > 15 and total_reviews >=1000 ')