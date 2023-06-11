import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import request
from flask import Flask


@app.route('/create', methods=['POST'])
def create_task():
    conn = None
    cursor = None
    try:        
        json = request.json
        title = json['title']
        description = json['description']
        duedate = json['duedate']
        status = json['status']

        if title and description and duedate and status and request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO task(title, description, duedate, status) VALUES(%s, %s, %s, %s)"
            bindData = (title, description, duedate, status)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Task added successfully!')
            response.status_code = 200
            return response
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close() 
        if conn is not None:
            conn.close()  
    return jsonify('Invalid request. Please use the POST method.'), 400        
   
     
@app.route('/task')
def task():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, title, description, duedate, status FROM task")
        taskRows = cursor.fetchall()
        response = jsonify(taskRows)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  

@app.route('/task/<int:task_id>')
def task_details(task_id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT id, title, description, duedate, status FROM task WHERE id =%s", task_id)
        taskRow = cursor.fetchone()
        response = jsonify(taskRow)
        response.status_code = 200
        return response
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 

@app.route('/update/', methods=['PUT'])
def update_task():
    conn = None
    cursor = None
    try:
        json = request.json
        id = json['id']
        title = json['title']
        description = json['description']
        duedate = json['duedate']
        status = json['status']
        if title and description and duedate and status and id and request.method == 'PUT':
            sqlQuery = "UPDATE task SET title=%s, description=%s, duedate=%s, status=%s WHERE id=%s"
            bindData = (title, description, duedate, status, id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            response = jsonify('Task updated successfully!')
            response.status_code = 200
            return response
        else:
            response = jsonify('Invalid request. Please provide all the required fields.')
            response.status_code = 400
            return response
    except Exception as e:
        print(e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()
    return jsonify('Invalid request. Please use the PUT method.'), 400


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete_task(id):
	try:
		conn = mysql.connect()
		cursor = conn.cursor()
		cursor.execute("DELETE FROM task WHERE id =%s", (id,))
		conn.commit()
		response = jsonify('Task deleted successfully!')
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close() 
		conn.close()
        
       

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

if __name__ == '__main__':
     app.run(debug=True)
        

