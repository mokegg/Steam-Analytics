# -*- coding: utf-8 -*-
from app import app
import os

if __name__ == '__main__':
    port = of.environ.get('PORT', 5000) #Heroku will set env variable to web traffic
    app.run(host="0.0.0.0", debug=False)

