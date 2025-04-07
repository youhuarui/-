from flask import Flask
from routes import bp

import os
template_folder = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__, template_folder=template_folder)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
