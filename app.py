from flask import Flask, render_template, url_for, flash, redirect, request
from forms import UserRegistrationForm, AdminRegistrationForm, UserLoginForm, AdminLoginForm
import pandas as pd
from flask_table import Table, Col, LinkCol, ButtonCol, BoolCol
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

pwd = os.getcwd()
file_path = os.path.join(pwd, 'static', 'data', 'zillow.csv')
print(file_path)

df = pd.read_csv(file_path)
print(df.head())
print(df.columns)

class ItemTable(Table):
    classes = ['highlight']
    index = Col('index')
    beds = Col('beds')
    year = Col('year')
    saved = BoolCol('Saved', yes_display='Yes', no_display='No')
    col1 = LinkCol('Edit', 'welcome', url_kwargs=dict(id='index'), anchor_attrs={'class': 'waves-effect waves-light btn-small'})
    #col2 = ButtonCol('Edit', 'welcome', url_kwargs=dict(id='index'), button_attrs={'class': 'waves-effect waves-light btn-small'})

items = []
for index, row in df.iterrows():
    print(row)
    print(str(row.Index), str(row[' Beds']))
    item = dict(index=str(row['Index']), beds=str(row[' Beds']), year=str(row[' Year']), saved=True)
    items.append(item)

new_table = ItemTable(items)

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    id= request.args.get('id')
    print('index', id)
    user_form = UserLoginForm(prefix="user")
    admin_form = AdminLoginForm(prefix="admin")
    if user_form.validate_on_submit():
        if user_form.email.data == 'admin@blog.com' and user_form.password.data == 'password':
            flash('You have logged in!', 'green green-text')
            return redirect(url_for('welcome', user_form=user_form))
        else:
            flash('Invalid credential, please check Email and Password!', 'red red-text')
    if admin_form.validate_on_submit():
        if admin_form.email.data == 'admin@blog.com' and admin_form.password.data == 'password':
            flash('You have logged in!', 'green green-text')
            return redirect(url_for('welcome', admin_form=admin_form))
        else:
            flash('Invalid credential, please check Email and Password!', 'red red-text')
    return render_template('welcome.html', user_form=user_form, admin_form=admin_form, id=id)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'green green-text')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register')

@app.route("/table")
def table():
    return render_template('table.html', title='table', new_table=new_table)

if __name__ == '__main__':
    app.run(debug=True)
