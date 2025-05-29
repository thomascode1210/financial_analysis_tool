import hashlib
import random
import string

# Hàm băm mật khẩu (Sẽ được quét là phần dễ hiểu, an toàn)
def hash_password(password):
    if not password:
        raise ValueError("Password cannot be empty.")
    return hashlib.sha256(password.encode()).hexdigest()

# Hàm tạo mật khẩu ngẫu nhiên
def generate_password(length=12):
    if length < 8:
        raise ValueError("Password too short.")
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(characters) for _ in range(length))

# Hàm login đơn giản (SonarCloud có thể gợi ý về security khi thiếu kiểm tra xác thực thực tế)
def login(username, password):
    print(f"Logging in as {username}...")  # Logging debug
    hashed = hash_password(password)
    # Giả sử ta có mật khẩu hardcoded để test security hotspot
    stored_hash = "5e88489da4..."  # Not safe!
    return hashed == stored_hash

# Hàm chứa code smell: dùng eval nguy hiểm
def run_custom_command(command):
    print("Running:", command)
    try:
        result = eval(command)  # Sonar sẽ cảnh báo eval là nguy hiểm
        return result
    except Exception as e:
        print("Command failed:", e)
        return None

# Hàm dài & lồng nhau (Sonar có thể đánh giá phức tạp)
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

# Gọi hàm để đảm bảo test coverage kiểm tra được
if __name__ == "__main__":
    pw = generate_password()
    print("Generated password:", pw)
    print("Hashed password:", hash_password(pw))

    result = login("admin", "password123")
    print("Login result:", result)

    custom = run_custom_command("2 + 2")
    print("Eval result:", custom)

    sample_tx = [
        {"type": "deposit", "amount": 100},
        {"type": "withdrawal", "amount": 50},
        {"type": "withdrawal", "amount": 70}
    ]
    print("Final balance:", process_transactions(sample_tx))
