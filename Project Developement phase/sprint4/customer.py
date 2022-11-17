from flask import Flask,render_template
app=Flask(__name__)

@app.route('/welcome')
def home():
    return render_template('welcome.html')

@app.route('ADMIN LOGIN')
def signin():
    return render_template('ADMIN LOGIN.html')

@app.route('/rectify')
def about():
    return render_template('rectify.html')


    
    
if __name__ =='_main_':
app.run(debug=True)