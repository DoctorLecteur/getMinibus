# -*- coding: utf-8 -*-
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'test123'}
    posts = [
        {
            'author': {'username': 'Вован'},
            'body': 'Test1'
        },
        {
            'author': {'username': 'Русик'},
            'body': 'Test2'
        },
        {
            'author': {'username': 'Димас'},
            'body': 'Test3'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)