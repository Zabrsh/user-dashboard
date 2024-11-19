import sys
import os
from flask import Flask
from flask_cors import CORS

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from server import app  # type: ignore

# Enable CORS for your Flask app
CORS(app)

if __name__ == '__main__':
    app.run(port=5000)