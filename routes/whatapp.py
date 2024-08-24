import os
from flask import Flask, Blueprint, request
import threading
from services.whatsapp_browser import send_message, setup_browser
from logs.logging_config import setup_logging
logger = setup_logging()

app = Flask(__name__)

whatapp_blueprint = Blueprint('whatapp', __name__)

@whatapp_blueprint.route("/send_message", methods=["POST"])
def send_message_route():
    phone_numbers = request.form["phone_numbers"].split(",")
    message = request.form["message"]
    driver = setup_browser()
    if driver:
        for phone_number in phone_numbers:
            process = threading.Thread(target=send_message, args=(driver, phone_number, message)).start()
            print('threading')
            print(process)
        return "Message sent successfully!"
    else:
        message = "Error setting up browser"
        logger.info(f"{message}")
        return message
app.register_blueprint(whatapp_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8181)