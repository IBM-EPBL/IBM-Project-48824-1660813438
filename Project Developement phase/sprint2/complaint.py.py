from flask import flask,render_template
app=flask(__name__)
@app.route("/")
def index():
    return render_template("complaint.html")
if __name__ =='_main_':
    app.run(debug=True)