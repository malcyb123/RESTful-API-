## RESTful-API-

## Document the necessary steps to set up and run the application locally.

### Installation of packages and libraries:

1) Go to VSCODE terminal or command prompt:
2) If using VS Code terminal, activate the base environment using **conda activate base.**
3) Install the required packages and libraries by running the following commands:
pip install flask
pip install flask-cors
pip install pymysql
pip install flask-mysql

## Installation of POSTMAN:
1) Open your browser and go to postman.com.
2) Sign in or create a new account.

## DataBase SetUp:
For MYSQL Database connection, make a 'assignment' named database and a 'task' named table with the structure:

CREATE TABLE task (
  id INT(11) NOT NULL AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  description TEXT,
  duedate DATE,
  status ENUM('Incomplete', 'In Progress', 'Completed'),
  PRIMARY KEY (id)
);


**Or** can also add in the SQL section put these query:

( ALTER TABLE `emp`
  ADD PRIMARY KEY (`id`);
  
ALTER TABLE `emp`
 MODIFY `id` int(11) NOT NULL AUTO_INCREMENT; )
 
 **Note:** host, port, username, and password provided in config.py
 
 ## RUNNING THE APPLICATION:
1) Open the terminal.
2) Navigate to the project directory.
3) Run the command python main.py to start the application.
 
## Endpoints:
1) Inside Postman create a collection and then click on the plus icon
2) Select the appropriate HTTP method for each endpoint and enter the corresponding URL:
### 1) Create a new task.
Select 'POST' method for 'create' and put this URL http://127.0.0.1:5000/create
( In the body section select raw and set the format to "JSON" the put this:
{
  "id": "Task id"
  "title": "Task Title",
  "description": "Task Description",
  "duedate": "2023-06-10",
  "status": "In Progress"
}
**Note:** ( Replace task ID with actual ID )
### 2) Retrieve a single task by its ID.
Select 'GET' method for 'listing tasks by ID' and put this URL http://127.0.0.1:5000/task/1

### 3) List all tasks.
Select 'GET' method for 'listing all tasks' and put this URL http://127.0.0.1:5000/task

### 4) Update an existing task.
Select 'GET' method for 'update' and put this URL http://127.0.0.1:5000/update
( In the body section select raw and set the format to "JSON" the put this:
{
  "id": "Task id for updating"
  "title": "Task update",
  "description": "Task Description update",
  "duedate": "2023-06-10",
  "status": "In Progress update"
}
**Note:** Replace task ID with actual ID 

### 5) Delete a task.
Select 'DELETE' method for 'delete' and put this URL http://127.0.0.1:5000/delete/2














