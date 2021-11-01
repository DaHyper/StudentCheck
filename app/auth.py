from flask import Blueprint, render_template, redirect, url_for, request
from studentvue import StudentVue

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
  return render_template('auth/login.html')
