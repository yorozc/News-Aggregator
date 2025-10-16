from flask import render_template, redirect, Blueprint, url_for, flash, request, session

auth = Blueprint('auth', __name__)