from flask import Flask,request

app = Flask(__name__)

@app.route('/student/<studentName>')
def getStudentName (studentName) :
    return 'Hello %s' % studentName

@app.route('/class/<className>')
def getClassName (className):
    return 'Your Class is %s' % className

@app.post('/class')
@app. route ('/class ', methods=[" POST"])
def processClassDetails():
    studentName = request.form['studentName']
    className = request.form['className']
    return 'Hello ' + studentName + ' you are in ' + className + ' class!'

@app.post("/student")
def processStudentDetail():
    studentAge = request. form['studentAge']
    studentName = request. form['studentName']
    return '<H1>Hi ' + studentName + ' you are ' + studentAge + ' years old!</H1>'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask,request
# import sqlite3
# app = Flask(__name__)
#
# @app.route('/books', methods=['GET','POST'])
# def insertBook():
#     conn = sqlite3.connect('books.sqlite')
#     cursor = conn.cursor()
#
#     if request.method == 'GET':
#         sql_search = """SELECT title,language FROM books"""
#         cursor.execute(sql_search)
#         books = cursor.fetchall()
#         return {"books": books}, 200
#
#     elif request.method == 'POST':
#         request_data = request.get_json()
#         new_book = {
#             "title": request_data['title'],
#             "author": request_data['author'],
#             "language": request_data['language']
#         }
#         sql_query = """INSERT INTO books (title, author, language) VALUES (?, ?, ?)"""
#         cursor.execute(sql_query, (new_book['title'], new_book['author'], new_book['language']))
#         conn.commit()
#         return new_book, 201
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#
