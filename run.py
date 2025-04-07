from flask import Flask
from routes import bp
import os

base_dir = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    __name__,
    template_folder=base_dir,       # 直接指向根目录
    static_folder=base_dir          # 同样，静态文件也在根目录
)
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
