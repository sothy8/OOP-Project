
# Clothes Management System

## Overview

This project is a web-based Clothes Management System that implements object-oriented programming (OOP) principles using Django. The application is designed to help manage clothing items efficiently, offering features such as adding, updating, and deleting items, as well as user authentication for secure access.

## Features

- **Clothing Item Management**: Add, update, delete, and view clothing items.
- **User Authentication**: Secure login and registration system for managing access.
- **Category Support**: Organize clothing items by categories (e.g., Men, Women, Kids).
- **Search and Filter**: Easily find items using search functionality and filters.
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices.

## Installation

### Prerequisites

- Python 3.x
- Django 3.x
- Git

### Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/sothy8/OOP-Project.git
   cd OOP-Project
   ```

2. **Create and Activate Virtual Environment**:

   - **MacOS/Linux**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - **Windows**:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser** (for accessing the Django admin panel):

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**:

   ```bash
   python manage.py runserver
   ```

   Access the application at `http://127.0.0.1:8000/`.

## Usage

- **Access the Admin Panel**: Navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.
- **Manage Clothing Items**: Use the admin interface to add, edit, or delete clothing items.
- **Search and Filter**: Use the search bar and filters on the frontend to find specific clothing items.
- **User Registration and Login**: Register a new user or log in with existing credentials to access user-specific features.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Official Website](https://www.python.org/)
