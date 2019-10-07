from flask import Flask, render_template, url_for, flash, redirect
from forms import UserRegistrationForm, AdminRegistrationForm, UserLoginForm, AdminLoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
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
    return render_template('welcome.html', user_form=user_form, admin_form=admin_form)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'green green-text')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register')


if __name__ == '__main__':
    app.run(debug=True)
