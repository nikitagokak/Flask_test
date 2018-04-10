#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 08:15:36 2018

@author: nikigokak
"""

def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str , letters:str = 'aeiou')-> set:
    """Return set of letters found in phrase"""
    return set(letters).intersection(set(phrase))