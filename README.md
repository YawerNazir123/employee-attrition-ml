Employee Attrition Prediction System

Machine Learning | Flask | SQL | Admin Dashboard

📌 Overview

The Employee Attrition Prediction System is a full-stack Machine Learning web application designed to predict whether an employee is at risk of leaving an organization.
The system uses a trained Random Forest Classifier and provides a probability-based risk score, helping HR teams make data-driven retention decisions.

The application includes a secure admin dashboard where all predictions are stored, analyzed, and visualized.

🚀 Key Features

Machine Learning model trained on HR data

Attrition risk score (%) using prediction probabilities

User-friendly web interface built with Flask

SQLite database to store all predictions

Admin-only dashboard with authentication

Analytics dashboard with summary metrics and charts

Deployed using GitHub + Render

🧠 Machine Learning Details

Algorithm: Random Forest Classifier

Target Variable: Employee Attrition (Yes / No)

Selected Features for Deployment:

Age

Monthly Income

Job Satisfaction

Work Life Balance

Total Working Years

Years at Company

Years with Current Manager

The model was retrained using only stable numerical features to ensure consistent inference during deployment.

🏗️ Tech Stack

Programming Language: Python

ML Library: scikit-learn

Web Framework: Flask

Database: SQLite

Frontend: HTML, CSS, Chart.js

Deployment: Render

Version Control: Git & GitHub

🔐 Admin Dashboard

Secure admin login (session-based authentication)

View all stored predictions

Summary cards:

Total predictions

High-risk employees

Low-risk employees

Pie chart visualization of attrition risk distribution

Logout functionality

⚙️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/YawerNazir123/employee-attrition-ml.git
cd employee-attrition-ml

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Application
python app.py


Open in browser:

http://127.0.0.1:5000

🌐 Live Demo

🔗 Live URL: (https://employee-attrition-ml-n56d.onrender.com)
🔗 GitHub Repo: https://github.com/YawerNazir123/employee-attrition-ml



Note: Credentials are hardcoded for demonstration.
In production, credentials should be stored securely using environment variables and password hashing.

📈 Use Cases

HR analytics and workforce planning

Identifying high-risk employees

Data-driven retention strategies

Learning real-world ML deployment

📚 Learning Outcomes

End-to-end ML deployment

Feature selection for production ML systems

Flask backend development

SQL database integration

Authentication & role-based access control

Cloud deployment workflow

🧑‍💻 Author

Shah Yawar
GitHub: https://github.com/YawerNazir123
