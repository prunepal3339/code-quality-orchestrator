from output.codestral.Task181_MISTRAL_codestral_latest import BankAccount

# Test cases
def test_bank_account():
    # Test 1: Create a new account with an initial balance
    account = BankAccount(1000)
    assert account.balance == 1000  # Initial balance should be correct

    # Test 2: Deposit money into the account
    account.deposit(500)
    assert account.balance == 1500  # Balance should be updated correctly

    # Test 3: Withdraw money from the account
    assert account.withdraw(200) == True
    assert account.balance == 1300  # Balance should reflect the withdrawal

    # Test 4: Withdraw more money than available (should fail)
    assert account.withdraw(2000) == False
    assert account.balance == 1300  # Balance should remain unchanged

    # Test 5: Deposit a negative amount (should raise an error)
    try:
        account.deposit(-100)
        assert False  # Should not reach this line
    except ValueError as e:
        assert str(e) == "Deposit amount must be positive"

    # Test 6: Close the account
    account.close()
    assert account.is_open == False  # Account should be marked as closed

    # Test 7: Try to deposit into a closed account (should raise an error)
    try:
        account.deposit(500)
        assert False  # Should not reach this line
    except RuntimeError as e:
        assert str(e) == "Account is closed"

    # Test 8: Try to withdraw from a closed account (should raise an error)
    try:
        account.withdraw(100)
        assert False  # Should not reach this line
    except RuntimeError as e:
        assert str(e) == "Account is closed"

    # Test 9: Close the account again (should still be closed)
    account.close()  # Should not raise an error
    assert account.is_open == False  # Still closed

    # Test 10: Create another account and check balance
    new_account = BankAccount(2000)
    assert new_account.balance == 2000  # New account should have correct balance

    print("All tests passed!")

# Run the test cases
test_bank_account()