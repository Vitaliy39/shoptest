from flask import Flask, render_template,  request, redirect, url_for
from shop.views import shop_blueprint
from user.views import user_blueprint
from common.database import Database
from jinja2 import TemplateNotFound

#print("hello")
app = Flask(__name__)
#app.register_blueprint(shop_blueprint, url_prefix='/shop')
app.register_blueprint(user_blueprint, url_prefix='/user')

@app.route('/', methods=['GET', 'POST'] )
def home():
     if request.method == 'POST':
          username = request.form['username']
          usertype = request.form['usertype']
          user_list = Database.find_by_name_and_job(username, usertype)
          if user_list[2] == 'user':
               return redirect(url_for('user.personal_index', user=str(user_list[1])))
          elif user_list[2] == 'manager':
               return redirect(url_for('manager.index'))
          elif user_list[2] == 'courier':
               return redirect(url_for('courier.index'))
     return render_template('home.html')

if __name__ == "__main__":
     app.run(debug=True)