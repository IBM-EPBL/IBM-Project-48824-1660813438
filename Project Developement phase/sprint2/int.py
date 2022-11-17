from flask import Flask,render_template
app=Flask(__name__)

@app.route('/welcome')
def home():
    return render_template('welcome.html')

@app.route('/ADMIN LOG')
def signin():
    return render_template('ADMIN LOGIN.html')

@app.route('/complaint')
def about():
    return render_template('complaint.html')

@app.route('/post.html')
def signup():
    return render_template('post.html')
if __name__ =='_main_':
app.run(debug=True)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=8081, debug=True)