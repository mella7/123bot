from views.webhook import webhook_bp
from views.dashboard import dashboard_bp 

from flask import Flask, request

app = Flask(__name__)

app.register_blueprint(dashboard_bp)
app.register_blueprint(webhook_bp)

if __name__ == '__main__':
    app.run(debug=True)