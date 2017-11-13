"""
slack server side
"""

# coding: utf-8


from flask import Flask, redirect, request
app = Flask(__name__)

@app.route("/")
def hello():
  "default"
  return redirect("http://honyamorake.ml:3000", code=302)

@app.route("/slack", methods=['POST', 'GET'])
def slack():
  "slack response"
  if request.method == "POST":
    name = "confirm"
    # print(request.headers)
    # print("body: %s" % request.form)
    json = """
    {
    "text": "*bold* `code` _italic_ ~strike~",
    "username": "markdownbot",
    "mrkdwn": true
    }
    """
    return json
  else:
    name = "plz send POST"
  return name

if __name__ == "__main__":
  app.run(debug=True, port=6000)
