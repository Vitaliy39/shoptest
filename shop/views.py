from flask import Blueprint, render_template, request

shop_blueprint = Blueprint('shop', __name__, template_folder = 'templates', static_folder = 'static')


#@shop_blueprint.route('/', methods=['GET', 'POST'])
#def index():
#    return render_template('shop/index.html')




