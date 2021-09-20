from flask import Flask
from cyclicmy.cyclicmy import main

app = Flask(__name__)


@app.route("/")
def hello():
    main()
    return "Hello World!"


if __name__ == "__main__":
    app.run()
