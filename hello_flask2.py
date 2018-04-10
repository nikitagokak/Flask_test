#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 22:32:58 2018

@author: nikigokak
"""

from flask import Flask
from vsearch import search4letters 
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return'Hello world from Flask!'

@app.route('/search4')
def do_search()-> str:
    return str(search4letters('life,the universe,the everything','eiru,!'))
app.run()
    