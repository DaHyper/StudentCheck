from flask import Blueprint, render_template, request, redirect, url_for
from studentvue import StudentVue

bp = Blueprint('sv', __name__)

@bp.route('/', methods=["GET", "POST"])
def index():

  user = None
  username = request.form.get("username")
  password = request.form.get("password")
  domain_name = request.form.get("domain-name")
  domain = "portal.{}.org".format(domain_name)
  domain = domain_name.split("-")[1].strip()
  try:
    user = StudentVue(username, password, domain)
  except:
    if user is None: 
      return redirect(url_for("auth.login"))
    else:
      return redirect(url_for('sv.index'))

  return render_template("main/index.html")

