from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"

@app.route("/burst")
def burst():
    ans = []
    for i in range(0, 100):
        response = requests.get("http://127.0.0.1:5000")
        ans.append(response.json)
        print(response.json)
    return "Done!!! 100 requests"
    
if __name__ == "__main__":
    app.run(debug=True)