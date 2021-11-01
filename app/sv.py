from flask import Blueprint, render_template, request, redirect, url_for, flash
from studentvue import StudentVue

from .utils import get_courses, get_upcoming_assignments, get_valid_schedule, grade_prediction

import datetime

bp = Blueprint('sv', __name__)

@bp.route('/', methods=["GET", "POST"])
def index():
  # handling auth
  user = None
  courses = None
  next_week = None
  schedule = None
  prediction = None


  tommorow = (datetime.date.today() + datetime.timedelta(days=1)).strftime("%m/%d/%Y")
  try:
    username = request.form.get("username")
    password = request.form.get("password")
    domain_name = request.form.get("domain-name")
    domain = domain_name.split("-")[1].strip()
    try:
      user = StudentVue(username, password, domain)
      user.get_gradebook()["Gradebook"]
    except:
        return redirect(url_for("auth.login"))

    # main code
    courses = get_courses(user)

    next_week = get_upcoming_assignments(user)
    schedule = get_valid_schedule(user)

    prediction = grade_prediction(user)

  except AttributeError:
    return redirect(url_for("auth.login"))

  return render_template("main/index.html",
                        user=user,
                        username=user._username, 
                        courses=courses,
                        next_week=next_week,
                        schedule=schedule,
                        prediction=prediction,
                        tommorow=tommorow)

