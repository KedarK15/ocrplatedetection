import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import cv2
import numpy as np
import easyocr
import imutils
from werkzeug.utils import secure_filename

# Use environment variable for database path or use in-memory SQLite
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///license_plates.db')
app.config['UPLOAD_FOLDER'] = os.path.join(os.path.dirname(__file__), 'uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Rest of your existing app.py code remains the same...

# Add this at the end to prevent running server when imported
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()