# Todo List

A simple **Todo List** web application built with Django. Allows creating, editing, deleting tasks and managing tags.

---

## Features

### Tasks
- Create, update, delete tasks.
- Display task information:
  - Task content (`content`)
  - Creation datetime (`created_at`)
  - Optional deadline (`deadline`)
  - Completion status (`is_done`)
  - Tags associated with the task
- Task ordering:
  - **Not done tasks first**, then **done tasks**
  - Newest tasks appear at the top
- **Complete / Undo** buttons to toggle task status

### Tags
- Create, update, delete tags
- Tags can be linked to multiple tasks (Many-to-Many)
- Display tags in a table view

---

## Interface
- **Base template (`base.html`)** inherited by all pages
- **Sidebar** with links:
  - Home
  - Tags
- Pages:
  - Home (`/`) – task list
  - Tags (`/tags/`) – tag list
  - Create / Update / Delete tasks and tags

---

## Technologies
- Python 3.11
- Django 5.2
- SQLite (default)
- HTML/CSS for templates

---

## Installation & Run

1. Clone the repository:
    ```bash
    git clone <https://github.com/RodionDem/task-tracker.git>
    cd task-tracker

---

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Mac/Linux
    venv\Scripts\activate     # Windows

---

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
   
---

4. Run migrations and start the server:
     ```bash
    python manage.py migrate
    python manage.py runserver

---

5. Open in browser:
    http://127.0.0.1:8000/
   
---

## Project Structure
    ```bash
    
    task-tracker/
    ├─ manage.py
    ├─ task_tracker/        # Django settings
    ├─ tasks/               # Tasks app
    │  ├─ migrations/
    │  ├─ models.py
    │  ├─ views.py
    │  ├─ urls.py
    │  └─ templates/tasks/
    │      ├─ task_list.html
    │      ├─ task_form.html
    │      ├─ task_confirm_delete.html
    │      ├─ tag_list.html
    │      ├─ tag_form.html
    │      └─ tag_confirm_delete.html
    ├─ templates/base.html
    └─ requirements.txt
