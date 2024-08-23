from flask import Flask, render_template
from routes.whatapp import whatapp_blueprint
from selenium.webdriver.support import expected_conditions as EC

app = Flask(__name__)
app.register_blueprint(whatapp_blueprint)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8181)