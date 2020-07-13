from flask import Flask, jsonify, request

#Creates the Flask application object
#This name is used to find resources on the filesystem, can be used by extensions to improve debugging information and a lot more.
app = Flask(__name__)

app.config["DEBUG"] = True

@app.route('/', methods = ['GET'])
def home():
    return 'Welcome to Flask Rest API'

ListOfColors = [
	{
        'id': 1,
		'color': "red",
		'value': "#f00"
	},
	{
        'id': 2,
		'color': "green",
		'value': "#0f0"
	},
	{
        'id': 3,
		'color': "blue",
		'value': "#00f"
	},
	{
        'id': 4,
		'color': "cyan",
		'value': "#0ff"
	},
	{
        'id': 5,
		'color': "magenta",
		'value': "#f0f"
	}
]

@app.route('/colors', methods = ['GET'])
def getColors():
    # if there is any params then we're getting data as find by ID else getting all list of colors
    if 'id' in request.args:
        id = int(request.args['id'])
        gotResultById = []
        for colors in ListOfColors:
            if(colors['id'] == id):
                gotResultById.append(colors)
        if(gotResultById):
            return jsonify(gotResultById)
        else:
            return jsonify({ 'message': 'No color found'})
    else:
        return jsonify(ListOfColors)


# adding static colors (POST method)
@app.route('/colors', methods = ['POST'])
def addColors():
    jsonData = request.json
    print(f'this is json Data {jsonData}')
    if not jsonData or not 'id' in jsonData or not 'color' in jsonData or not 'value' in jsonData:
        return abort(400)
    else:
        ListOfColors.append(jsonData)
        return jsonify(ListOfColors)

#handling 404 not found pages
@app.errorhandler(404)
def pageNotFound(error):
    return 'Page not found :('


@app.errorhandler(400)
def abort(err):
    return 'invalid values !! '

app.run()