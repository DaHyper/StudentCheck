from flask import Blueprint, render_template, request, redirect, url_for, flash
from studentvue import StudentVue

from .utils import get_courses, get_upcoming_assignments, get_valid_schedule, grade_prediction, get_current_lesson, is_holiday

import datetime

# importing pandas in order to read the schools.csv files
import pandas as pd

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
        df = pd.read_csv("app/schools.csv")
        schools = dict(zip(df["SchoolName"], df["DomainName"]))
        username = request.form.get("username")
        password = request.form.get("password")
        domain_name = request.form.get("domain-name")
        domain = schools[domain_name]
        try:
            user = StudentVue(username, password, domain)
            user.get_gradebook()["Gradebook"]
        except:
            flash("Incorrect Credentials")
            return redirect(url_for("auth.login"))

        # main code
        courses = get_courses(user)

        next_week = get_upcoming_assignments(user)
        schedule = get_valid_schedule(user)

        prediction = grade_prediction(user)

        current_lesson = get_current_lesson(user)
        today_holiday = is_holiday(user)

    except KeyError:
     return redirect(url_for("auth.login"))

    return render_template("main/index.html",
                           user=user,
                           username=user._username,
                           courses=courses,
                           next_week=next_week,
                           schedule=schedule,
                           prediction=prediction,
                           tommorow=tommorow,
                           current_lesson=current_lesson,
                           today_holiday=today_holiday)
