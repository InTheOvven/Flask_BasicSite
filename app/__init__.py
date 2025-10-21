from flask import Flask

#Sets variable app to this folder (also named app) so we can import other scrips on launch
app = Flask(__name__)

from app import routes
