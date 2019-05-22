from flask import Flask, render_template, request
from form.form import UserForm

from dao.helper import *

app = Flask(__name__)
app.secret_key = 'development key'


@app.route('/', methods=['GET', 'POST'])
def user():
    form = UserForm()
    helper = update()

    if request.method == 'POST':
        status, NAME_D = helper.delUser(
            NAME=request.form["name"],
            POPULATION=request.form["population"]
        )
        print(status)
        print(NAME_D)
    return render_template('user.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)