from output.gtp4o.Task181_OPENAI_gpt_4o import BankAccount

def test_bank_account():
    # Test 1: Create a new account with an initial balance
    account = BankAccount(id="12345", balance=1000)
    assert account.balance == 1000  # Initial balance should be correct

    # Test 2: Deposit money into the account
    new_balance = account.deposit(500)
    assert new_balance == 1500  # Balance should be updated correctly

    # Test 3: Withdraw money from the account
    new_balance = account.withdraw(200)
    assert new_balance == 1300  # Balance should reflect the withdrawal

    # Test 4: Withdraw more money than available (should return "Insufficient funds")
    result = account.withdraw(2000)
    assert result == "Insufficient funds"  # Should return the appropriate message

    # Test 5: Deposit a negative amount (should still succeed, but handle it in practice)
    new_balance = account.deposit(-100)

    assert new_balance == 1300  # Balance should remain unchanged in this implementation

    # Test 6: Close the account
    result = account.close()
    assert result == "Account closed"  # Account should be marked as closed
    assert account.closed == True  # Verify the account is indeed closed

    # Test 7: Try to deposit into a closed account (should return "Account is closed")
    result = account.deposit(500)
    assert result == "Account is closed"  # Should return the appropriate message

    # Test 8: Try to withdraw from a closed account (should return "Account is closed")
    result = account.withdraw(100)
    assert result == "Account is closed"  # Should return the appropriate message

    # Test 9: Close the account again (should still be closed)
    result = account.close()  # Should not raise an error but return "Account closed"
    assert result == "Account closed"  # Still should return that the account is closed

    # Test 10: Create another account and check balance
    new_account = BankAccount(id="67890", balance=2000)
    assert new_account.balance == 2000  # New account should have correct balance

    print("All tests passed!")

# Run the test cases
test_bank_account()