#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:57:18 2018

@author: nikigokak
"""

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello() -> str:
    return'Hello world from Flask!'
app.run()
    