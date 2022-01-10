# -*- coding: utf-8 -*-
from app import app

@app.route('/')
@app.route('/index')

def index():
    return "Привет, Мир!"