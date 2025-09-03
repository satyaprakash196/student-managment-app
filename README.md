# Student Management System

A simple **Student Management System** built with **Flask**, **MySQL**,  store detail in database 
This project is containerized with **Docker** and deployed on **Kubernetes**.

---

## 🚀 Features
- Add new students with details (Name, Age, Mobile, Email, Course)
- Automatically send **SMS notification** to the student after enrollment
- Data stored in **MySQL database**
- **Responsive form** with Flask web interface
- Kubernetes ready with Deployment and Service manifests

---

## 🛠 Tech Stack
- **Frontend:** HTML, CSS (Flask Templates)
- **Backend:** Python (Flask)
- **Database:** MySQL
- **Containerization:** Docker
- **Orchestration:** Kubernetes (k8s)

---

## 📂 Project Structure
student-management/
│
├── app.py # Flask application
├── Dockerfile # Docker build file
├── requirements.txt # Python dependencies
├── kubernetes/
│ ├── flask-deployment.yaml
│ ├── flask-service.yaml
│ ├── mysql-deployment.yaml
│ └── mysql-service.yaml
└── README.md

Installation & Setup:
git clone https://github.com/<your-username>/student-management.git
cd student-management

1 Build Docker image
2- push docker images docker hub

MySQL Setup:
Login to MySQL and create a database:
kubectl exit -it pod-name -n name -- bash
mysql -u root -p    = password root databe

CREATE DATABASE school;
USE school;
CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    mob VARCHAR(15),
    email_id VARCHAR(100),
    course VARCHAR(50)
);

Create a user and grant permissions:
CREATE USER 'myuser'@'%' IDENTIFIED BY 'myuser@123';
GRANT ALL PRIVILEGES ON school.* TO 'myuser'@'%';
FLUSH PRIVILEGES;



