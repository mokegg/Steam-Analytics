#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 18:38:05 2021

@author: mokegg
"""

from flask import Flask

app = Flask(__name__)

from app import routes