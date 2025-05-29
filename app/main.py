import hashlib
import secrets  # Thêm dòng này
import string

def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty.")
    return hashlib.sha256(password.encode()).hexdigest()

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password too short.")
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(secrets.choice(characters) for _ in range(length))

def login(username, password, stored_hash):
    print(f"Logging in as {username}...")
    hashed = hash_password(password)
    return hashed == stored_hash

def run_custom_command(command):
    print("Running:", command)
    try:
        result = eval(command)
        return result
    except Exception as e:
        print("Command failed:", e)
        return None

def process_transactions(transactions):
    total = 0
    for t in transactions:
        if t["type"] == "deposit":
            total += t["amount"]
        elif t["type"] == "withdrawal":
            if t["amount"] > total:
                print("Insufficient funds.")
            else:
                total -= t["amount"]
        else:
            print("Unknown transaction type:", t["type"])
    return total

if __name__ == "__main__":
    pw = generate_password()
    print("Generated password:", pw)
    print("Hashed password:", hash_password(pw))

    stored_hash = hash_password("password123")
    result = login("admin", "password123", stored_hash)
    print("Login result:", result)

    custom = run_custom_command("2 + 2")
    print("Eval result:", custom)

    sample_tx = [
        {"type": "deposit", "amount": 100},
        {"type": "withdrawal", "amount": 50},
        {"type": "withdrawal", "amount": 70}
    ]
    print("Final balance:", process_transactions(sample_tx))
