from flask import Blueprint, redirect, url_for, render_template

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/', methods=['GET'])
def index():
    return redirect(url_for('admin.login'))


@admin.route('/login', methods=['GET'])
def login():
    return render_template('admin/login.html')
