from flask import Flask, request, jsonify

app = Flask(__name__)

# Initial data
data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]


@app.route('/items', methods=['GET', 'POST', 'DELETE'])
def items():
    if request.method == 'GET':
        return jsonify(data)  # Return the data in JSON format

    elif request.method == 'POST':
        new_item = request.get_json()  # Get data from POST request
        data.append(new_item)  # Add the new item to the data list
        return jsonify({'message': 'Item is added successfully'})

    elif request.method == 'DELETE':
        item_to_delete = request.get_json()  # Get data from DELETE request
        item_id = item_to_delete.get('id')
        item = next((item for item in data if item["id"] == item_id), None)
        if item:
            data.remove(item)  # Remove the item from the data list
            return jsonify({'message': 'Item is deleted successfully'})
        else:
            return jsonify({'message': 'Item not found'}), 404  


if __name__ == '__main__':
    app.run(debug=True)
