from flask import flask,render_template
app=flask(__name__)
@app.route("/")
def index():
    return render_template("welcome.html")
if __name__ =='_main_':
    app.run(debug=True)