# Project Setup Guide

## Project Overview
MerchFlow is an advanced eCommerce API platform designed to streamline the management of user accounts, product catalogs, orders, and categories. This project empowers developers to build scalable and efficient eCommerce systems seamlessly integrated into their applications.

## Technologies Used
- **Backend**: Django (Python)
- **Database**: MySQL
- **Version Control**: Git and GitHub
- **Authentication**: JWT, Basic Auth, Cookie Auth

---

## Installation

### Step 1: Clone the Repository
Clone the project repository to your local machine using the following command:
```bash
git clone https://github.com/mahmoud9797/Graduation_project.git
```

### Step 2: Navigate to the Project Directory
Change your working directory to the project folder:
```bash
cd E_commerce
```

### Step 3: Configure the Database
Update the database configuration:
- **Django**: Modify `settings.py` to include your database credentials.
- **Alternative**: Use a `.env` file to store sensitive information securely.

### Step 4: Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### Step 5: Apply Migrations
Run the following commands to apply database migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Run the Development Server
Start the server using the following command:
```bash
python manage.py runserver
```

### Step 7: Access the Platform
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

---

## Usage
1. **Register or Log In**: Create an account or log in as a user.
2. **Browse Products**: Explore the product catalog and categories.
3. **Manage Orders**: Place orders, track shipments, and manage your cart.
4. **Dashboard**: View and track your activity, purchases, and account details.

---

## Contribution
We welcome contributions from the community to enhance MerchFlow. To contribute:

1. **Fork the Repository**: Create a copy of the project on your GitHub account.
2. **Create a New Branch**: For your feature or bug fix:
    ```bash
    git checkout -b feature-name
    ```
3. **Commit Your Changes**: Add your changes and commit them:
    ```bash
    git commit -m "Add feature-name"
    ```
4. **Push to Your Fork**: Push your branch to your forked repository:
    ```bash
    git push origin feature-name
    ```
5. **Open a Pull Request**: Navigate to the original repository and create a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
