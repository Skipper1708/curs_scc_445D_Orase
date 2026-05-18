from flask import Flask
from app.routes.paris import paris_bp

app = Flask(__name__)

app.register_blueprint(paris_bp)


@app.route("/")
def index():
    return "Aplicatia Orase ruleaza. Acceseaza /orase pentru tema proiectului."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
