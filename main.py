import helper
from flask import Flask, request, Response
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
   return 'Hello World!'


@app.route('/users/new', methods = ['POST'])
def add_user():
   #Get users from the POST body
   req_data = request.get_json()
   username = req_data['username']
   
   #Add user to the list
   res_data = helper.add_to_user(username)

   #Return error if user not added
   if res_data is None:
      response = Response("{'error': 'User not added - '}"  + username, status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

@app.route('/posts/new', methods = ['POST'])
def add_post():
   #Get users from the POST body
   req_data = request.get_json()
   text = req_data['text']
   user_id = req_data['user_id']
   
   #Add user to the list
   res_data = helper.add_to_post(text, user_id)

   #Return error if user not added
   if res_data is None:
      response = Response("{'error': 'Post not added - '}"  + text, status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

@app.route('/posts/all')
def get_all_posts():
   # Get posts from the helper
   res_data = helper.get_all_posts()
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   return response

@app.route('/users/all')
def get_all_users():
   # Get posts from the helper
   res_data = helper.get_all_users()
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   return response

@app.route('/post', methods=['GET'])
def get_post():
   #Get parameter from the URL
   id = request.args.get('id')
   
   # Get posts from the helper
   post = helper.get_post(id)
   
   #Return 404 if post not found
   if post is None:
      response = Response("{'error': 'Post Not Found - '}"  + post, status=404 , mimetype='application/json')
      return response

   #Return status
   res_data = {
      'text': post
   }

   response = Response(json.dumps(res_data), status=200, mimetype='application/json')
   return response

@app.route('/post/update', methods = ['PUT'])
def update_post():
   #Get post from the POST body
   req_data = request.get_json()
   id = int(req_data['id'])
   text = req_data['text']
   
   #Update post in the list
   res_data = helper.update_post(id, text)
   if res_data is None:
      response = Response("{'error': 'Error updating post - '""}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response

@app.route('/post/remove', methods = ['DELETE'])
def delete_post():
   #Get post from the POST body
   req_data = request.get_json()
   id = int(req_data['id'])
   
   #Delete post from the list
   res_data = helper.delete_post(id)
   if res_data is None:
      response = Response("{'error': 'Error deleting post - '""}", status=400 , mimetype='application/json')
      return response
   
   #Return response
   response = Response(json.dumps(res_data), mimetype='application/json')
   
   return response