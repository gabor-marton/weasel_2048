from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = 'so amazingly secret'  # for session values

@app.route("/")
def main():
    return render_template('index.html')
    
import alone_2048
