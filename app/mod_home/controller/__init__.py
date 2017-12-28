# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, flash, jsonify, Response
from app import app

mod_home = Blueprint('home', __name__, url_prefix='/home')

@mod_home.route('/', methods=['GET', 'POST'])
def get_home():
    return render_template("home.html")


@mod_home.route('/info', methods=['GET', 'POST'])
def get_info():
    return jsonify({
        "Name": "Manuel Hernández Mota",
        "Phone": "3316002870",
        "Email": "manuelhdzmota@outlook.com"
    })

@mod_home.route('/sendEmail', methods=['GET'])
def send_email():
    return "TEST STRING"