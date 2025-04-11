
# very simple flask server

from flask import Flask, request

app = Flask(__name__)

# Home page
@app.route('/')
def index():
        return "Hello world"

# Get all books
@app.route('/books', methods=['GET'])
def getall():
        return "Get all"

# Get a book by id
@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return "find by id"

# Create a book
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsontring = request.json
        return f"create {jsontring}"

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsontring = request.json
        return f"update {id} {jsontring}"

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return f"delete {id}"


if __name__ == "__main__":
    app.run(debug = True)
