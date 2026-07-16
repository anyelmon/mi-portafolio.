import re

def password_analyzer(password):
    score = 0
    problems = []
    weak_passwords = ["password", "123456", "qwerty", "abc123", "admin", "letmein", "welcome", "monkey", "login", "passw0rd"]

    if len(password) >= 8:
        score += 1
    else:
        problems.append("Too short (minimum 8 characters)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        problems.append("No uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        problems.append("No lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        problems.append("No numbers")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        problems.append("No special characters")

    if score <= 2:
        level = "WEAK"
    elif password.lower() in weak_passwords:
        level = "WEAK"
    elif score <= 4:
        level = "MEDIUM"
    else:
        level = "STRONG"

    return level, score, problems

while True:
    password = input("\nEnter a password (or 'exit' to quit): ")
    password = password.strip()
    if password == "exit":
        break
    level, score, problems = password_analyzer(password)
    print(f"Level: {level} ({score}/5)")
    if problems:
        print("Problems found:")
        for p in problems:
            print(f"  - {p}")