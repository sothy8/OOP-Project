# OOP-Project

## Overview

This project focuses on implementing object-oriented programming (OOP) concepts using Django to create a web application for managing products such as books or other items.

## Setup

### Clone the Repository
Clone the repository:
```bash
git clone https://github.com/sothy8/OOP-Project.git
cd OOP-Project
```

### Create and Activate Virtual Environment
Create the virtual environment (if not already created):
```bash
python3 -m venv venv
```

Activate the virtual environment:
- **MacOS/Linux**:
  ```bash
  source venv/bin/activate
  ```
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```

### Install Dependencies
Install all required dependencies:
```bash
pip install -r requirements.txt
```

### Deactivate Virtual Environment
Once done, deactivate the virtual environment:
```bash
deactivate
```

### Pull Updates (If You Already Have the Repo Setup)
Fetch the latest changes:
```bash
git fetch origin
```

Merge the changes into your local branch:
```bash
git merge origin/main
```

Alternatively, use:
```bash
git pull
```

---

## Folder Structure

```
OOP-Project/
├── Product_OOP/             # Main project folder
│   ├── settings.py          # Project settings
│   ├── urls.py              # URL routing
│   └── wsgi.py              # WSGI application entry point
│
├── product/                 # Django app for items (e.g., books/products)
│   ├── migrations/          # Database migration files
│   ├── models.py            # Database models
│   ├── views.py             # Views for the app
│   ├── urls.py              # App-specific URLs
│   └── admin.py             # Admin configurations
│
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## How to Contribute

1. Create a new branch:
   ```bash
   git checkout -b feature-branch-name
   ```

2. Make your changes and commit:
   ```bash
   git commit -m "Description of changes"
   ```

3. Push the branch:
   ```bash
   git push origin feature-branch-name
   ```

4. Open a pull request.

---

## How to Update the Virtual Environment

1. Activate the virtual environment:
   - **MacOS/Linux**:
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```

2. Install new packages as needed:
   ```bash
   pip install package_name
   ```

3. Update `requirements.txt` with the new packages:
   ```bash
   pip freeze > requirements.txt
   ```

4. Deactivate the virtual environment:
   ```bash
deactivate
```

5. Commit and push the updated `requirements.txt`:
   ```bash
   git add requirements.txt
   git commit -m "Update requirements.txt with new packages"
   git push origin main
   ```

---

## Updating Files

### Update Jupyter Notebook Files
1. Add the notebook file:
   ```bash
   git add your_notebook.ipynb
   ```
2. Commit the changes:
   ```bash
   git commit -m "Update Jupyter Notebook with new changes"
   ```
3. Push the changes:
   ```bash
   git push origin main
   ```

### Update Python Files
1. Add the Python file:
   ```bash
   git add your_file.py
   ```
2. Commit the changes:
   ```bash
   git commit -m "Update Python file with new changes"
   ```
3. Push the changes:
   ```bash
   git push origin main
   ```
