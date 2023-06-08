from flask import Flask
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
# print("Current Time =", current_time)

app = Flask(__name__)

@app.route("/")
def index():
  return "<h1>Hello the current time is: " + current_time + "</h1>"

if __name__ == "__main__":
  app.run(debug=True)