from flask import Flask,render_template
app=Flask(__name__)

@app.route('/welcome')
def home():
    return render_template('welcome.html')

@app.route('agentlog')
def signin():
    return render_template('agentlog.html')

@app.route('/com')
def about():
    return render_template('com.html')

@app.route('/Agentsolution')
def signup():
    return render_template('Agentsolution.html')
 @app.route('/posted')
def signup():
    return render_template('posted.html')
    
    
if __name__ =='_main_':
app.run(debug=True)