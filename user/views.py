from flask import  render_template, Blueprint


user_blueprint = Blueprint('user', __name__, template_folder = 'templates', static_folder = 'static')

@user_blueprint.route('/', methods=['GET', 'POST'])
def index():
    return render_template('user/index.html')
