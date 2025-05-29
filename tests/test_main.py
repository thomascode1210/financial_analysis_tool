from app.main import generate_password, hash_password, login, run_custom_command, process_transactions

def test_generate_password():
    pw = generate_password(12)
    assert len(pw) == 12
    assert any(c.isdigit() for c in pw)
    assert any(c.isalpha() for c in pw)
    assert any(c in "!@#$%^&*()" for c in pw)

def test_run_custom_command_allowed():
    assert run_custom_command("2 + 2") == 4
    assert run_custom_command("3 * 3") == 9

def test_run_custom_command_not_allowed():
    assert run_custom_command("os.system('rm -rf /')") is None

def test_login_with_correct_hash():
    password = "test123"
    stored_hash = hash_password(password)
    assert login("user", password, stored_hash) is True

def test_login_with_incorrect_hash():
    stored_hash = hash_password("correctpass")
    assert login("user", "wrongpass", stored_hash) is False

def test_process_transactions_insufficient_funds():
    tx = [
        {"type": "deposit", "amount": 50},
        {"type": "withdrawal", "amount": 100}
    ]
    assert process_transactions(tx) == 50

def test_process_transactions_valid():
    tx = [
        {"type": "deposit", "amount": 100},
        {"type": "withdrawal", "amount": 50}
    ]
    assert process_transactions(tx) == 50
