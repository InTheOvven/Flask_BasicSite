from app import app

#This is file that allows us to define sub-directories on our website
#We probably rename index to resource-directory or something similar later
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
