from flask import Flask, render_template, request, redirect, url_for, session
import numpy as np
import joblib
from database import get_connection, create_table

app = Flask(__name__)
app.secret_key = "super_secret_admin_key"

model = joblib.load("employee_attrition_prediction.pkl")
create_table()

# ADMIN CREDENTIALS
ADMIN_EMAIL = "yawarshah.work@gmail.com"
ADMIN_PASSWORD = "yawer@123"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict", methods=["GET", "POST"])
def predict():
    prediction = None
    risk = None

    if request.method == "POST":
        age = int(request.form["Age"])
        income = int(request.form["MonthlyIncome"])
        js = int(request.form["JobSatisfaction"])
        wlb = int(request.form["WorkLifeBalance"])
        twy = int(request.form["TotalWorkingYears"])
        yac = int(request.form["YearsAtCompany"])
        ywm = int(request.form["YearsWithCurrManager"])

        features = np.array([[age, income, js, wlb, twy, yac, ywm]])
        probability = model.predict_proba(features)[0][1]
        risk = round(probability * 100, 2)

        prediction = "High Risk of Attrition" if risk >= 50 else "Low Risk of Attrition"

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO employee_predictions (
                age, monthly_income, job_satisfaction,
                work_life_balance, total_working_years,
                years_at_company, years_with_manager,
                risk_score, prediction
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (age, income, js, wlb, twy, yac, ywm, risk, prediction))
        conn.commit()
        conn.close()

    return render_template("predict.html", prediction=prediction, risk=risk)

# ---------- ADMIN LOGIN ----------
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid admin credentials"

    return render_template("admin_login.html", error=error)

# ---------- DASHBOARD (PROTECTED) ----------
@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    conn = get_connection()
    cursor = conn.cursor()

    records = cursor.execute(
        "SELECT * FROM employee_predictions ORDER BY created_at DESC"
    ).fetchall()

    total = cursor.execute(
        "SELECT COUNT(*) FROM employee_predictions"
    ).fetchone()[0]

    high_risk = cursor.execute(
        "SELECT COUNT(*) FROM employee_predictions WHERE prediction='High Risk of Attrition'"
    ).fetchone()[0]

    low_risk = cursor.execute(
        "SELECT COUNT(*) FROM employee_predictions WHERE prediction='Low Risk of Attrition'"
    ).fetchone()[0]

    conn.close()

    return render_template(
        "dashboard.html",
        records=records,
        total=total,
        high_risk=high_risk,
        low_risk=low_risk
    )

# ---------- LOGOUT ----------
@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return render_template("about.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
