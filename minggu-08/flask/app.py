from flask import Flask, render_template, request, session


app = Flask(__name__)
app.config['SECRET_KEY'] = "tesSession90"

@app.route('/')
def index():
    #looping
    fruit = ['banana', 'strawbery', 'apple', 'mango', 'orange']
    #condition
    condition = "happy"

    return render_template('index.html', nilai=fruit, condition=condition)

#extend route
@app.route('/about')
def about():
    return render_template ('about.html')

#parsing int
@app.route('/number/<int:number>')
def number(number):
    return "number is : {}".format(number)

#parsing string
@app.route('/name/<string:name>')
def name(name):
    return "name is : {}".format(name)

#parsing argument
@app.route('/argumentparser')
def argumentparser():
    data = request.args.get("number")
    return "what is the number parser is : {}".format(data)

#session start
@app.route('/halaman/<int:nilai>')
def login(nilai):
    session["nilaiku"] = nilai
    return "success set session"

#session views
@app.route('/halaman/views')
def view_session():
    data = session['nilaiku']
    return "session set is : {}".format(data)

#session destroy
@app.route('/halaman/logout')
def logout():
    session.pop('nilaiku')
    return "success logut"

if __name__ == "__main__":
    app.run(debug=True)