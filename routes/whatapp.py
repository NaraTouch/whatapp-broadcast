from flask import Flask, Blueprint
import threading
from services.whatsapp_browser import send_message, setup_browser
from logs.logging_config import logging

app = Flask(__name__)

whatapp_blueprint = Blueprint('whatapp', __name__)

@whatapp_blueprint.route("/send_message", methods=["POST"])
def send_message_route():
    phone_number = ["+85517694939","+85581470095"]
    message = "Hello, this is a test message!"
    driver = setup_browser()
    if driver:
        threading.Thread(target=send_message, args=(driver, phone_number, message)).start()
        message = "Message sent successfully!"
        logging.info(f"{message}")
        return message
    else:
        message = "Error setting up browser"
        logging.info(f"{message}")
        return message

app.register_blueprint(whatapp_blueprint)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8181)