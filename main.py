from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route('/books', methods=['GET','POST'])
def insertBook():
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()

    if request.method == 'GET':
        sql_search = """SELECT title,language FROM books"""
        cursor.execute(sql_search)
        books = cursor.fetchall()
        return {"books": books}, 200

    elif request.method == 'POST':
        request_data = request.get_json()
        new_book = {
            "title": request_data['title'],
            "author": request_data['author'],
            "language": request_data['language']
        }
        sql_query = """INSERT INTO books (title, author, language) VALUES (?, ?, ?)"""
        cursor.execute(sql_query, (new_book['title'], new_book['author'], new_book['language']))

        conn.commit()
        return new_book, 201

@app.route('books/<int:id>', methods=['PUT'])
def update_Book(id, request_json=None):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()

    update_Book = {
        "title": request_json['title'],
        "author": request_json['author'],
        "language": request_json['language']
    }

    sql_query = """UPDATE books GET title = ?, author = ? WHERE id = ?"""
    cursor.execute(sql_query,(update_Book['title'], update_Book['author'], update_Book['language'], id))
    conn.commit()
    return update_Book, 200

@app.route('books/<int:book_id', methods=['DELETE'])
def delete_Book(book_id):
    conn = sqlite3.connect('books.sqlite')
    cursor = conn.cursor()


    sql_query = """DELETE FROM books WHERE id = ?"""
    cursor.execute(sql_query, (book_id,))
    conn.commit()
    return {"message": "Book has been deleted successfully"}, 200



if __name__ =='__main__':
    app.run(debug=True)
