from flask import Flask
from routes import bp
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'templates'),
    static_folder=os.path.join(base_dir, 'static')
)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
