from flask import Flask, request, render_template, redirect, url_for
from form import Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

@app.route("/", methods=['GET','POST'])
def hello_world():
  request_method = request.method
  if request.method == 'POST':
    first_name = request.form['firstname']
    return redirect(url_for('name', first_name=first_name))
  return render_template('hello.html', request_method=request_method)

@app.route('/<string:first_name>')
def name(first_name):
  return render_template('base.html', first_name=first_name)

@app.route('/todo', methods=['GET', 'POST'])
def todo():
  todo_form = Todo()
  if todo_form.validate_on_submit():
    print(todo_form.content.data)
    return redirect('/')
  return render_template('todo.html', form=todo_form)

if __name__ == '__main__':
  app.run(debug=True)

  