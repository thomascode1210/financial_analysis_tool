from app.main import (
    login,
    generate_password,
    run_custom_command,
    process_transactions,
)

def test_login():
    password = "mypassword"
    stored = hash_password(password)

    assert login("user", password, stored) is True
    assert login("user", "wrongpass", stored) is False

def test_hash_password():
    pw = "hello123"
    hashed = hash_password(pw)
    assert isinstance(hashed, str)
    assert len(hashed) == 64

def test_generate_password():
    pw = generate_password(12)
    assert len(pw) == 12
    assert any(c.isdigit() for c in pw)
    assert any(c.isalpha() for c in pw)

def test_login():
    assert login("user", "password") is False

def test_run_custom_command_safe():
    assert run_custom_command("3 * 3") == 9

def test_run_custom_command_invalid():
    assert run_custom_command("bad_code@@@") is None

def test_process_transactions():
    tx = [
        {"type": "deposit", "amount": 100},
        {"type": "withdrawal", "amount": 30},
        {"type": "withdrawal", "amount": 80},
        {"type": "unknown", "amount": 50}
    ]
    assert process_transactions(tx) == 70
