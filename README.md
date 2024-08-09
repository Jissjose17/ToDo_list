ToDo List Application - README
Introduction
This repository contains a simple ToDo List application built using Django, a powerful and flexible Python web framework. The application provides a CRUD (Create, Read, Update, Delete) interface for managing tasks in a to-do list. It allows users to add, view, update, and delete tasks, helping them manage their daily activities efficiently.

Features
Add Tasks: Create new tasks with a title and description.
View Tasks: View all tasks in the to-do list.
Update Tasks: Edit the details of existing tasks.
Delete Tasks: Remove tasks that are no longer needed.
Mark Tasks as Completed: Mark tasks as completed to keep track of progress.
Technologies Used
Python 3.x
Django 3.x
SQLite3 (default database for Django)
Installation
Prerequisites
Before you begin, ensure you have the following installed on your local machine:

Python 3.x
pip (Python package installer)
virtualenv (recommended)
Steps to Install
Clone the Repository:

bash
Copy code
git clone https://github.com/Jissjose17/ToDo_list.git
cd ToDo_list
Create and Activate a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py migrate
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application:
Open your web browser and go to http://127.0.0.1:8000/.

Usage
Once the server is running, you can start using the ToDo List application:

Add a Task:

Navigate to the "Add Task" page.
Enter the task title and description.
Click "Add Task" to save it.
View All Tasks:

The homepage displays a list of all tasks.
Each task shows its title, description, and status (completed or not).
Update a Task:

Click the "Edit" button next to the task you want to update.
Modify the task details and save changes.
Delete a Task:

Click the "Delete" button next to the task you want to remove.
Mark a Task as Completed:

Click the "Complete" button to mark a task as completed.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
