from output.gemini.Task181_GEMINI_gemini_1_5_pro_001 import BankAccount

def test_bank_account():
    # Test 1: Create a new account with an initial balance
    account = BankAccount(1000)
    assert account.get_balance() == 1000  # Initial balance should be correct

    # Test 2: Deposit money into the account
    account.deposit(500)
    assert account.get_balance() == 1500  # Balance should be updated correctly

    # Test 3: Withdraw money from the account
    account.withdraw(200)
    assert account.get_balance() == 1300  # Balance should reflect the withdrawal

    # Test 4: Withdraw more money than available (should raise an error)
    try:
        account.withdraw(2000)
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Insufficient funds."

    # Test 5: Deposit a negative amount (should raise an error)
    try:
        account.deposit(-100)
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Deposit amount must be positive."

    # Test 6: Close the account
    account.close()
    assert account.is_open == False  # Account should be marked as closed

    # Test 7: Try to deposit into a closed account (should raise an error)
    try:
        account.deposit(500)
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Cannot deposit to a closed account."

    # Test 8: Try to withdraw from a closed account (should raise an error)
    try:
        account.withdraw(100)
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Cannot withdraw from a closed account."

    # Test 9: Close the account again (should raise an error)
    try:
        account.close()
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Account is already closed."

    # Test 10: Open the account again (should raise an error)
    try:
        account.open()
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Account is already open."

    print("All tests passed!")

# Run the test cases
test_bank_account()