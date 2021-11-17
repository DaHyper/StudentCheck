from flask import Blueprint, render_template, redirect, url_for, request

import pandas as pd

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
  df = pd.read_csv("app/schools.csv")
  counties = df["SchoolName"].astype(str)
  
  return render_template('auth/login.html', counties=counties)
