# -*- coding: utf-8 -*-
from flask import render_template, redirect
from app import app

@app.route("/gallery")
def gallery_view():
    render_template("gallery.html")
