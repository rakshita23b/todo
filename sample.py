# Dictionary-based login example
users = {
    "user1": "pass123",
    "admin": "admin@123",
    "student": "school2024",
}


def check_login(data):
    username = data.get("user")
    password = data.get("password")

    if not username:
        return "Username is missing. Please enter a user name."

    if not password:
        return "Password is missing. Please enter a password."

    if username not in users:
        return f"User '{username}' does not exist."

    if password != users[username]:
        return f"Password is wrong for user '{username}'. Please check the password and try again."

    return f"Login successful! Welcome, {username}."


# Example dictionary input
user_input = {
    "user": "admin",
    "password": "wrongpassword"
}

print(check_login(user_input))

