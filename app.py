from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL = '/api-docs'
API_URL = '/static/swagger.json'

swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={})
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

book_list = [
    {"isbn": "1234567890", "title": "Sample Book", "author": "John Doe", "year": 2020, "genre": "Fiction"}
]

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    
    if 'title' not in data or 'author' not in data or 'year' not in data or 'isbn' not in data:
        return jsonify({"error": "Missing required fields"}), 400
    
    new_book = {
        "isbn": data["isbn"],
        "title": data["title"],
        "author": data["author"],
        "year": data["year"],
        "genre": data.get("genre", "")
    }
    
    book_list.append(new_book)
    return jsonify(new_book), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(book_list), 200

@app.route('/books/search', methods=['GET'])
def search_books():
    author = request.args.get('author')
    year = request.args.get('year')
    genre = request.args.get('genre')

    filtered_books = book_list

    if author:
        filtered_books = [book for book in filtered_books if author.lower() in book['author'].lower()]
    
    if year:
        filtered_books = [book for book in filtered_books if str(book['year']) == year]
    
    if genre:
        filtered_books = [book for book in filtered_books if genre.lower() in book['genre'].lower()]

    return jsonify(filtered_books), 200

@app.route('/books/<isbn>', methods=['DELETE'])
def delete_book(isbn):
    global book_list
    book_list = [book for book in book_list if book['isbn'] != isbn]

    return jsonify({"message": "Book deleted"}), 204

@app.route('/books/<isbn>', methods=['PUT'])
def update_book(isbn):
    data = request.get_json()
    
    book = next((book for book in book_list if book['isbn'] == isbn), None)
    
    if book is None:
        return jsonify({"error": "Book not found"}), 404

    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['year'] = data.get('year', book['year'])
    book['genre'] = data.get('genre', book['genre'])

    return jsonify(book), 200

if __name__ == '__main__':
    app.run(debug=True)
