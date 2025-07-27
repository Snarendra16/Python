# HTTP verbs
# Working with API's -----> JSON file

from flask import Flask , jsonify ,redirect ,request 
app=Flask(__name__)

items=[
    {'id':1,'name':'Item 1','description':'This is item 1'},
    {'id':2,'name':'Item 2','description':'This is item 2'}
]

@app.route('/')
def home():
    return "Welcome to the basic TO-DO List Web app"

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

# REST API's

# GET Method ----> Getting items from list
@app.route('/items/<int:id>')
def get_item(id):
    item=next((item for item in items if item['id']==id),None)
    if item is None:
        return jsonify({'error': 'Item not found'})
    return jsonify(item)

# POST Method ----> Create new to-do
@app.route('/items',methods=['POST'])
def create_items():
    if not request.json or not 'name' in request:
        return jsonify({'error': 'Item not found'})
    new_item={
        'id': items[-1]['id']+1 if items else 1,
        'name': request.json['name'],
        'description': request.json['description','']
    }
    items.append(new_item)
    return jsonify(new_item)

# PUT ----> Update an existing list
@app.route('/items/<int:id>',methods=['PUT'])
def update_items(id):
    item=next((item for item in items if item['id']==id),None)
    if not request.json or not 'name' in request:
        return jsonify({'error': 'Item not found'})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE ----> Delete from exidting list
@app.route('/items/<int:id>',methods=['DELETE'])
def delete_item():
    global items
    item=[item for item in items if item['id']!=id]
    return jsonify({'Result':'Item deleted successfully'})

if __name__=='__main__':
    app.run(debug=True)