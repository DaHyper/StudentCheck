from flask import Blueprint, render_template, redirect, url_for, request
from studentvue import StudentVue

bp = Blueprint('auth', __name__)

@bp.route('/login')
def login():
  username = request.form.get("login-username")
  password = request.form.get('login-password')
  domain_name = request.form.get('login-domain-name')
  domain = "portal.{}.org".format(domain_name)

  try:
    user = StudentVue(username, password, domain)
    return redirect(url_for('sv.index({})'.format(user)))
  except:
    pass

  return render_template('auth/login.html')
