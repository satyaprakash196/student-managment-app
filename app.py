from flask import Flask, request, render_template_string
import mysql.connector

app = Flask(__name__)

# -----------------------------
# MySQL connection
# -----------------------------
db = mysql.connector.connect(
    host="mysql-service",
    user="myuser",
    password="myuser@123",
    database="school"
)
cursor = db.cursor()

# -----------------------------
# HTML template with CSS
# -----------------------------
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: #f0f4f8;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background: #ffffff;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            width: 350px;
        }
        h2 {
            text-align: center;
            color: #333;
        }
        input[type="text"],
        input[type="number"],
        input[type="email"] {
            width: 100%;
            padding: 10px 12px;
            margin: 8px 0;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
        }
        input[type="submit"] {
            width: 100%;
            background-color: #4CAF50;
            color: white;
            padding: 12px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 16px;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        p {
            text-align: center;
            color: #4CAF50;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Enter Student Details</h2>
        <form method="POST">
            Name: <input type="text" name="name" required><br>
            Age: <input type="number" name="age" required><br>
            Mobile: <input type="text" name="mob" required><br>
            Email: <input type="email" name="email" required><br>
            <input type="submit" value="Submit">
        </form>

        {% if message %}
        <p>{{ message }}</p>
        {% endif %}
    </div>
</body>
</html>
"""

# -----------------------------
# Flask route
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form["name"]
        age = request.form["age"]
        mob = request.form["mob"]
        email = request.form["email"]

        sql = "INSERT INTO student (name, age, mob, email_id) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, age, mob, email))
        db.commit()
        message = "Student added successfully!"

    return render_template_string(html, message=message)

# -----------------------------
# Run Flask app
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

