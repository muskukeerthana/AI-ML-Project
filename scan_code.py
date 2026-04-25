import os
import joblib
import re

# Load model
model = joblib.load("ml_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_code(code):
    code = re.sub(r'\bbad\b', 'METHOD', code)
    code = re.sub(r'\bgood\b', 'METHOD', code)
    return code

def static_analysis(code):
    issues = []
    if "executeQuery" in code or "Statement" in code:
        issues.append("Possible SQL Injection")
    return "; ".join(issues) if issues else "No issues"

def ml_analysis(code):
    cleaned = clean_code(code)
    X = vectorizer.transform([cleaned])
    pred = model.predict(X)[0]
    return "VULNERABLE" if pred == 1 else "SAFE"

report = []

for file in os.listdir():
    if file.endswith(".java"):
        with open(file, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()

        static_res = static_analysis(code)
        ml_res = ml_analysis(code)

        report.append(f"{file} - Static: {static_res} | ML: {ml_res}")

with open("security_report.txt", "w") as f:
    for line in report:
        f.write(line + "\n")

print("Scan complete. Check security_report.txt")