# -*- coding: utf-8 -*-
import pandas as pd
from pandas import json_normalize
import json
import sqlite3

from app import app

@app.route('/')
@app.route('/index')
def index():

    # Open JSON data
    with open("database.json") as f:
        data = json.load(f)
    
    df = pd.json_normalize(data.values(), max_level=2)
    Data= df['name'][0]
    return Data

@app.route('/Q')
def Q():

    # Open JSON data
    with open("database.json") as f:
        data = json.load(f)
    
    df = pd.json_normalize(data.values(), max_level=2)
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
    c.execute("""SELECT * FROM Table1 WHERE review_score >= 8 AND required_age= 18 AND total_reviews >=500""")
    result = []
    for row in c.fetchall():
        result.append(row)
    Result =pd.DataFrame(result, columns=['steam_appid', 'name', 'required_age', 'is_free', 'review_score', 'total_reviews'])
    Data=Result[['steam_appid', 'name', 'required_age', 'review_score', 'total_reviews']]
    #Data = Result.to_html('Result.html')
    return Data.to_html(header="true", table_id="table")