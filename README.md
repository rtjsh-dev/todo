# Django ToDo App

A simple and elegant task management web application built with Django 6.0.1. This application allows users to create, update, mark as complete/incomplete, and delete tasks with an intuitive user interface.

![Django](https://img.shields.io/badge/Django-6.0.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3.0-purple.svg)

## 📋 Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation & Setup](#installation--setup)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Project Overview](#project-overview)
- [Database Schema](#database-schema)
- [URL Configuration](#url-configuration)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

- ✅ **Create Tasks** - Add new tasks to your to-do list
- ✏️ **Edit Tasks** - Update existing task descriptions
- ✔️ **Mark as Done/Undone** - Toggle task completion status
- 🗑️ **Delete Tasks** - Remove tasks from the list
- 📊 **Separate Views** - View pending and completed tasks separately
- 📱 **Responsive Design** - Works seamlessly on desktop and mobile devices
- 🎨 **Clean UI** - Modern interface using Bootstrap 5
- ⏰ **Timestamp Tracking** - Automatic creation and update timestamps

## 📁 Project Structure

```
ToDoApp/
│
├── manage.py                 # Django's command-line utility
├── db.sqlite3               # SQLite database file
├── README.md                # Project documentation
│
├── todo_main/               # Main project configuration
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── views.py             # Home page view
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
│
├── ToDo/                    # ToDo app (main application)
│   ├── __init__.py
│   ├── admin.py             # Admin panel configuration
│   ├── apps.py              # App configuration
│   ├── models.py            # Database models (Task model)
│   ├── views.py             # Application views
│   ├── urls.py              # App-specific URL patterns
│   ├── tests.py             # Unit tests
│   └── migrations/          # Database migrations
│       ├── __init__.py
│       └── 0001_initial.py
│
├── templates/               # HTML templates
│   ├── home.html            # Main task list page
│   └── edit_task.html       # Task editing page
│
└── env/                     # Virtual environment (not in version control)
    ├── Scripts/
    ├── Lib/
    └── Include/
```

## 🛠️ Technologies Used

- **Backend Framework**: Django 6.0.1
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, Bootstrap 5.3.0
- **Icons**: Font Awesome 4.7.0
- **Python Version**: Python 3.x
- **Dependencies**:
  - asgiref==3.11.0
  - sqlparse==0.5.5
  - tzdata==2025.3

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **pip** (Python package installer) - Usually comes with Python
- **Git** (optional) - For cloning the repository

To verify your Python installation:

```bash
python --version
```

## 🚀 Installation & Setup

Follow these steps to set up the project on your local machine:

### Step 1: Clone or Download the Project

If using Git:

```bash
cd "C:/Users/ACER/OneDrive/Desktop/Lets Django"
git clone <repository-url>
cd ToDoApp
```

Or simply navigate to the project directory if you already have it:

```bash
cd "C:/Users/ACER/OneDrive/Desktop/Lets Django/ToDoApp"
```

### Step 2: Create a Virtual Environment

Creating a virtual environment is recommended to isolate project dependencies:

```bash
python -m venv env
```

### Step 3: Activate the Virtual Environment

Activate the virtual environment:

**On Windows (Git Bash/Bash):**

```bash
source env/Scripts/activate
```

**On Windows (Command Prompt):**

```cmd
env\Scripts\activate.bat
```

**On Windows (PowerShell):**

```powershell
env\Scripts\Activate.ps1
```

**On macOS/Linux:**

```bash
source env/bin/activate
```

You should see `(env)` prefix in your terminal prompt indicating the virtual environment is active.

### Step 4: Install Dependencies

Install all required packages:

```bash
pip install django==6.0.1
pip install sqlparse
pip install asgiref
pip install tzdata
```

Or if you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Step 5: Apply Database Migrations

Create the database tables by running migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

This will create the `db.sqlite3` database file and set up the Task table.

### Step 6: Create a Superuser (Optional)

To access the Django admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set username, email, and password.

## 🏃 Running the Application

### Start the Development Server

```bash
python manage.py runserver
```

You should see output similar to:

```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
February 01, 2026 - 10:00:00
Django version 6.0.1, using settings 'todo_main.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

### Access the Application

Open your web browser and navigate to:

- **Main Application**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Stopping the Server

Press `CTRL+C` in the terminal to stop the development server.

### Deactivating the Virtual Environment

When you're done working:

```bash
deactivate
```

## 💡 Usage

### Adding a Task

1. On the home page, locate the "Add New Task" input field
2. Type your task description
3. Click the "Add" button or press Enter
4. The task will appear in the "Pending Tasks" section

### Marking a Task as Done

1. Find the task in the pending tasks list
2. Click the "Mark as Done" button (green button with checkmark)
3. The task moves to the "Completed Tasks" section

### Marking a Task as Undone

1. Find the task in the completed tasks section
2. Click the "Mark as Undone" button
3. The task moves back to the pending tasks list

### Editing a Task

1. Click the "Edit" button (blue button) on any task
2. Modify the task description in the edit page
3. Click "Update" to save changes
4. You'll be redirected back to the home page

### Deleting a Task

1. Click the "Delete" button (red button) on any task
2. The task will be permanently removed from the database

## 🔍 Project Overview

### Application Architecture

This Django application follows the **MVT (Model-View-Template)** architecture pattern:

#### Models (`ToDo/models.py`)

The `Task` model represents a to-do item with the following fields:

- `task` - CharField (max 200 characters): The task description
- `is_Completed` - BooleanField: Task completion status
- `created_at` - DateTimeField: Automatic timestamp when task is created
- `updated_at` - DateTimeField: Automatic timestamp when task is modified

#### Views (`ToDo/views.py` & `todo_main/views.py`)

The application includes the following views:

1. **home** - Displays all tasks (pending and completed)
2. **addTask** - Handles task creation
3. **mark_as_done** - Marks a task as completed
4. **mark_as_undone** - Marks a task as incomplete
5. **edit_task** - Handles task editing (GET and POST)
6. **delete_task** - Deletes a task

#### Templates

- **home.html** - Main page displaying all tasks with action buttons
- **edit_task.html** - Form for editing existing tasks

### Key Features Explanation

#### Task Filtering

- Pending tasks are retrieved using: `Task.objects.filter(is_Completed=False)`
- Completed tasks use: `Task.objects.filter(is_Completed=True)`
- Tasks are ordered by `updated_at` to show recently modified tasks first

#### CSRF Protection

All forms include Django's CSRF token for security against Cross-Site Request Forgery attacks.

#### Responsive Design

The application uses Bootstrap 5's grid system and components for a mobile-friendly interface.

## 🗄️ Database Schema

### Task Model

| Field        | Type         | Description                  | Constraints       |
| ------------ | ------------ | ---------------------------- | ----------------- |
| id           | Integer      | Primary key (auto-generated) | Primary Key, Auto |
| task         | VARCHAR(200) | Task description             | Max Length: 200   |
| is_Completed | Boolean      | Completion status            | Default: False    |
| created_at   | DateTime     | Task creation timestamp      | Auto Add          |
| updated_at   | DateTime     | Last modification timestamp  | Auto Update       |

## 🔗 URL Configuration

### Main URLs (`todo_main/urls.py`)

- `/` - Home page (task list)
- `/admin/` - Django admin interface
- `/todo/` - ToDo app URLs (includes all task operations)

### ToDo App URLs (`ToDo/urls.py`)

- `/todo/addTask/` - Add a new task
- `/todo/mark_as_done/<int:pk>/` - Mark task as completed
- `/todo/mark_as_undone/<int:pk>/` - Mark task as incomplete
- `/todo/edit_task/<int:pk>/` - Edit a task
- `/todo/delete_task/<int:pk>/` - Delete a task

## 📸 Screenshots

### Home Page

The home page displays:

- Current date
- Input field to add new tasks
- List of pending tasks with action buttons
- List of completed tasks

### Task Management

Each task has three action buttons:

- **Green Button** (✓) - Mark as Done
- **Blue Button** (✏️) - Edit Task
- **Red Button** (🗑️) - Delete Task

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit your changes (`git commit -am 'Add new feature'`)
5. Push to the branch (`git push origin feature/improvement`)
6. Create a Pull Request

### Areas for Improvement

- Add user authentication and authorization
- Implement task categories/tags
- Add due dates and reminders
- Implement search and filter functionality
- Add task priority levels
- Create REST API endpoints
- Add unit and integration tests
- Implement dark mode
- Add task statistics and analytics

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Django Documentation](https://docs.djangoproject.com/)
2. Review the error messages in the terminal
3. Ensure all migrations are applied
4. Verify your virtual environment is activated

## 🙏 Acknowledgments

- Django Framework - [https://www.djangoproject.com/](https://www.djangoproject.com/)
- Bootstrap - [https://getbootstrap.com/](https://getbootstrap.com/)
- Font Awesome - [https://fontawesome.com/](https://fontawesome.com/)

---

**Made with 💖 By Rajesh Thapa**
