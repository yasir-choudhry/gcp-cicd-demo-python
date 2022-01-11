import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

test_num = 5
test_num_2 = 0
if test_num == 2:
    test_num_2 = 1
elif test_num == 3:
    test_num_2 = 2
elif test_num == 3:
    test_num_2 = 3
elif test_num == 4:
    test_num_2 = 4


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))