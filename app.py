"""
In this project we are going to simulate online store on the flask
"""


# from logging import raiseExceptions
from flask import Flask , jsonify, request, render_template  
app = Flask(__name__)    #  gives each file a name

stores = [
                {
                'name': 'My wonderful store' ,
                'items':
                        [
                            {
                            'name': 'My Item',
                            'price': 15.99
                            }
                        ]

                }

        ]



@app.route('/')
def home():
    return render_template('index.html')

#post on server: used to receive data
#get on server: used to send back the data 

#Post /Store data: {name}
@app.route('/store', methods = ['POST']) 
def create_store():
    request_data = request.get_json()     ##from where the data is coming 
    new_store = {
                    'name': request_data['name'],
                    'items': []
                }

    stores.append(new_store)
    return jsonify(new_store)



#Get /Store/ <string:name>
@app.route('/store/<string:name>')  #https://127.0.0.1:5000/store/item
def get_store(name):
    #Iterate over stores
    #If the store name matches, return it
    #If none match, return an error message
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})
            
#Get /Store 
@app.route('/store/')  #https://127.0.0.1:5000/store/item
def get_stores():
    return jsonify({'stores': stores})

#Post /Store/<string:name>/item{name:, price}
@app.route('/store/<string:name>/item', methods = ['POST']) 
def create_item_in_store(name):

    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:

            new_items = {
                    'name': request_data['name'],
                    'price': request_data['price']
                    
                        }
            store['items'].append(new_items)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

#GET /store/<string:name>/item
@app.route('/store/<string:name>/item')  #https://127.0.0.1:5000/store/item
def get_item_in_store(name):
    for store in stores:
        if stores['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'messsage': 'store not found'})


app.run(port= 5001)


