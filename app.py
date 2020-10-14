from flask import Flask, render_template, abort, request
from shop.views import shop_blueprint
from user.views import user_blueprint
from jinja2 import TemplateNotFound

#print("hello")
app = Flask(__name__)
app.register_blueprint(shop_blueprint, url_prefix='/shop')
app.register_blueprint(user_blueprint, url_prefix='/user')

@app.route('/', methods=['GET', 'POST'] )
def home():
     return render_template('home.html')



if __name__ == "__main__":
     app.run(debug=True)