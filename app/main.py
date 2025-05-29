import hashlib
import secrets
import string

def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty.")
    return hashlib.sha256(password.encode()).hexdigest()

def generate_password(length=12):
    if length < 8:
        raise ValueError("Password too short.")
    
    letters = string.ascii_letters
    digits = string.digits
    special_chars = "!@#$%^&*()"
    
    password = [
        secrets.choice(letters), 
        secrets.choice(digits), 
        secrets.choice(special_chars)  
    ]
    
    remaining_length = length - len(password)
    if remaining_length < 0:
        raise ValueError("Length must be at least 3 to include required characters.")
    
    all_chars = letters + digits + special_chars
    password.extend(secrets.choice(all_chars) for _ in range(remaining_length))
    
    secrets.SystemRandom().shuffle(password)
    
    return ''.join(password)

def login(username, password, stored_hash):
    print(f"Logging in as {username}...")
    hashed = hash_password(password)
    return hashed == stored_hash

def run_custom_command(command):
    print("Running:", command)
    allowed_commands = {
        "2 + 2": 4,
        "3 * 3": 9,
        "5 - 2": 3
    }
    if command in allowed_commands:
        return allowed_commands[command]
    else:
        print("Command not allowed:", command)
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
