# Steam-Analytics

## Description

The project is aimed at to visualizing the Steam dataset and deploy an app to answer the ultimate question: Is it worth investing more time into video games?

## Mission objectives

The objectives are consolidate the knowlege in Python, specifically in :

- Be able to parse json files
- Be able to build and deploy an app using Flask, docker, and heroku
- Be able to save json data into an SQL database
- Be able to design a relational SQL database
- Be able to visualize data from a SQL database
- Be able to deploy said database alongside (interactive) visualizations

### Must-have features

- at least one visualization on the data
- deployment using Flask+docker+heroku
- json parsing to SQL data (you can use any number of layers in between, e.g. json > python objects > SQL data)
- any SQL database framework
- data retrieval from SQL database

### Nice-to-haves

- a database having a relational structure, making use of primary keys, foreign keys,...
- interactive visualizations on the deployed site (e.g. genre filtering)
- timeseries visualizations
- gross/net revenu estimation using the [date-adjusted boxleiter method](https://vginsights.com/insights/article/how-to-estimate-steam-video-game-sales)

## Discussion
The must have features are achieved.
 

 1. A Flask app is developed with the following functions:   
  * The json file was imported to pandas
  * Data cleaning  and preparation is done in pandas
  * The cleaned data was saved to into an SQL database (sqlite3)
  * Data could be visualized from SQL database
  
 2. A docker image is built 
 3. The docker image is pushed to heroku.  

The app could be consulted here: [Heroku app](https://steam-mekonnen-app.herokuapp.com/v)

## Insights

It is very interesting that:
    

  * Only 80 games are responsible for generating 80% of the revenue
  * Only 14 games generate 50% of the revenue.

## Further Development
The database has only one table.  In addition, interactive visualizations are built on Dash-plotly but not with flask.  It would be nice to build a full fledge database with more tables and connections implemented.