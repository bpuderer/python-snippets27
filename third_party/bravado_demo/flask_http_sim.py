import argparse
from flask import Flask, request, jsonify, abort, url_for, make_response

#app = Flask(__name__)
app = Flask(__name__, static_url_path='')
books = []


def make_public_book(book):
    new_book = {}
    for field in book:
        new_book[field] = book[field]
    new_book['uri'] = url_for('get_book', bookid=book['identifier']['ISBN10'], _external=True)
    return new_book

@app.errorhandler(404)
def not_found(e):
    return make_response(jsonify({'error': 'Book not found'}), 404)

@app.errorhandler(400)
def bad_request(e):
    return make_response(jsonify({'error': 'Bad request'}), 400)

@app.errorhandler(409)
def conflict(e):
    return make_response(jsonify({'error': 'Book already exists'}), 409)

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify({'books': [make_public_book(book) for book in books]})

@app.route('/books/<bookid>', methods=['GET'])
def get_book(bookid):
    book = [book for book in books if book['identifier']['ISBN10'] == bookid]
    if book:
        return jsonify(book[0])
    else:
        abort(404)

@app.route('/books', methods=['POST'])
def create_book():
    if not request.json:
        abort(400)
    elif 'identifier' not in request.json or 'ISBN10' not in request.json['identifier'] or 'title' not in request.json:
        abort(400)
    #better to use duck typing
    elif type(request.json['identifier']['ISBN10']) != unicode or type(request.json['title']) != unicode:
        abort(400)
    elif not request.json['identifier']['ISBN10'].strip() or not request.json['title'].strip():
        abort(400)
    elif [book for book in books if book['identifier']['ISBN10'] == request.json['identifier']['ISBN10']]:
        abort(409)
    else:
        books.append(request.json)
        return jsonify(make_public_book(request.json)), 201

@app.route('/books/<bookid>', methods=['PUT'])
def update_book(bookid):
    if not request.json:
        abort(400)
    elif 'identifier' not in request.json or 'ISBN10' not in request.json['identifier'] or 'title' not in request.json:
        abort(400)
    #better to use duck typing
    elif type(request.json['identifier']['ISBN10']) != unicode or type(request.json['title']) != unicode:
        abort(400)
    elif not request.json['identifier']['ISBN10'].strip() or not request.json['title'].strip():
        abort(400)

    book = [book for book in books if book['identifier']['ISBN10'] == bookid]
    if not book:
        abort(404)
    book[0]['title'] = request.json['title']
    book[0]['identifier']['ISBN10'] = request.json['identifier']['ISBN10']
    return jsonify(make_public_book(book[0]))

@app.route('/books', methods=['DELETE'])
def delete_books():
    del books[:]
    return jsonify({'result': True})

@app.route('/books/<bookid>', methods=['DELETE'])
def delete_book(bookid):
    book = [book for book in books if book['identifier']['ISBN10'] == bookid]
    if book:
        books.remove(book[0])
        return jsonify({'result': True})
    else:
        abort(404)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="localhost")
    parser.add_argument("--port", type=int, default="1234")
    args = parser.parse_args()
    app.run(host=args.ip, port=args.port, debug=True)
