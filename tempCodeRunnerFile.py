import pickle
import re
import os
import gc  # Added missing import
import numpy as np
from datetime import datetime
import pandas as pd
import torchvision.transforms as transforms # type: ignore
from PIL import Image
import io 
import base64
from flask import Flask


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)