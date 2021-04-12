from flask import Flask, jsonify, abort, request, make_response

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

users = [
    {
        'id': 1,
        #These 'u' characters being appended to an object signifies that the object is encoded in "unicode"
        'username': u'grim_reaper1O1',
        'favourite_food': u'Pasta, Rice, Pizza, Chicken, Vegetables, Chinese'
    },
    {
        'id': 2,
        'username': u'dark_shadow',
        'favourite_food': u'Pasta, Rice, Pizza, Vegetables, Chinese'
    },
    {
        'id': 3,
        'username': u'liam',
        'favourite_food': u'Pasta, Rice, Pizza, Chicken, Vegetables, Chinese'
    },
    {
        'id': 4,
        'username': u'delta',
        'favourite_food': u'Pasta, Rice, Pizza, Chicken, Vegetables, Chinese'
    },
    {
        'id': 5,
        'username': u'now9',
        'favourite_food': u'Pasta, Rice, Pizza, Chicken, Vegetables, Chinese, pedigree'
    },
    {
        'id': 6,
        'username': u'delta',
        'favourite_food': u'Pasta, Rice, Pizza, Chicken, Vegetables, Chinese, oppai'
    },
    
]

@app.route('/home')
@app.route('/')
def index():
        return "FLASK API TESTING (Index Page)"


@app.route('/info')
def get_info():
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_with_id(user_id):
    user = [user for user in users if user['id'] == user_id] #list comprehension
    if(len(user)==0):
        abort(404) #http error code 404: Not found
    return jsonify(user[0])


#POST METHOD:(inserting new item)  [After importing 'request' module ]
#The 'request.json' will have the request data, but only if it came marked as JSON. If the data isn't there, or if it is there, but we are missing a 'username' item then we return an error code 400, which is the code for the bad request.
@app.route('/users/create', methods=['POST'])
def create_user():
    #python 'if not' means :  Python try to convert the object(here request.json) to a bool value if it is not already one
    if not request.json or not 'username' in request.json:
        abort(400) #HTTP Code 400: Bad Request
    
    #new user dictionary template:
    user = {
        'id': users[-1]['id'] +1,
        'username': request.json['username']
    }

    #We append the new task to our 'users' array, and then respond to the client with the added 'user' and send back a status code 201, which HTTP defines as the code for "Created".
    users.append(user)
    return jsonify( { 'user': user } ), 201


if __name__ == "__main__":
    app.run(debug=True)
