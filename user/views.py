from flask import render_template, Blueprint, request
from common.database import Database

user_blueprint = Blueprint('user', __name__, template_folder='templates', static_folder='static')


@user_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('user/index.html')


@user_blueprint.route('/<string:user>', methods=['GET', 'POST'])
def personal_index():
    data = Database.get_all_data('goods')
    if request.method == 'POST':
        new_data = request.form['chicken']
        print(new_data)
    return render_template('user/index.html', goods=data)
