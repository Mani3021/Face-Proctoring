from flask import Flask, render_template
import json
import werkzeug
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template('index.html',name=name)

@app.route('/exec')
def parse(name=None):
    import face_recognize
    print("done")
    return render_template('index.html',name=name)

@app.route('/exec2')
def parse1(name=None):
	import create_data
	print("done")
	return render_template('index.html',name=name)

# @app.route("/", methods=["POST"])
# def index():
#     import face_recognize
#     imagefile = request.files["image"]
#     filename = werkzeug.utils.secure_filename(imagefile.filename)
#     print("\nReceived image File name : " + imagefile.filename)
#     imagefile.save("datasets/" + filename)
#     faces = faces("./datasets/manish" + filename)
#     return json.dumps({"faces": faces})

if __name__ == '__main__':
    app.run(debug = True,port = 8000)
    