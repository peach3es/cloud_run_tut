import os
from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# Simulated in-memory data store
items = []

# Define routes for the RESTful API


# Retrieve all items (GET) or create a new item (POST)
@app.route("/items", methods=["GET", "POST"])
def items_collection():
    if request.method == "GET":
        # Return the list of items
        return jsonify(items), 200

    elif request.method == "POST":
        # Create a new item
        new_item = request.json
        if not new_item or not "name" in new_item:
            abort(400, description="Invalid item data")

        items.append(new_item)
        return jsonify(new_item), 201


# Retrieve, update, or delete a specific item by ID
@app.route("/items/<int:item_id>", methods=["GET", "PUT", "DELETE"])
def item_resource(item_id):
    if item_id >= len(items) or item_id < 0:
        abort(404, description="Item not found")

    if request.method == "GET":
        # Return the specific item
        return jsonify(items[item_id]), 200

    elif request.method == "PUT":
        # Update the specific item
        updated_item = request.json
        if not updated_item or not "name" in updated_item:
            abort(400, description="Invalid item data")

        items[item_id] = updated_item
        return jsonify(updated_item), 200

    elif request.method == "DELETE":
        # Delete the specific item
        deleted_item = items.pop(item_id)
        return jsonify(deleted_item), 200


@app.route("/", methods=["GET"])
def hello_world():
    """Example Hello World route."""
    return "Hello World!!!!!!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
