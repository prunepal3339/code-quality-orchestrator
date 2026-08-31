from output.llama3.Task181_PERPLEXITY_llama_3_sonar_large_32k_chat import BankAccount


def test_bank_account():
    # Test 1: Create a new account with an initial balance
    account = BankAccount(initial_balance=1000)
    assert account.get_balance() == 1000  # Initial balance should be correct

    # Test 2: Deposit money into the account
    assert account.deposit(500) == True  # Deposit should succeed
    assert account.get_balance() == 1500  # Balance should be updated correctly

    # Test 3: Withdraw money from the account
    assert account.withdraw(200) == True  # Withdrawal should succeed
    assert account.get_balance() == 1300  # Balance should reflect the withdrawal

    # Test 4: Withdraw more money than available (should return False)
    assert account.withdraw(2000) == False  # Should fail
    assert account.get_balance() == 1300  # Balance should remain unchanged

    # Test 5: Close the account
    account.close_account()
    assert account.closed == True  # Account should be marked as closed

    # Test 6: Try to deposit into a closed account (should return False)
    assert account.deposit(500) == False  # Should fail
    assert account.get_balance() == 1300  # Balance should remain unchanged

    # Test 7: Try to withdraw from a closed account (should return False)
    assert account.withdraw(100) == False  # Should fail
    assert account.get_balance() == 1300  # Balance should remain unchanged

    # Test 8: Open the account again
    account.open_account()
    assert account.closed == False  # Account should be marked as open

    # Test 9: Deposit into the opened account
    assert account.deposit(500) == True  # Should succeed
    assert account.get_balance() == 1800  # Balance should reflect the deposit

    # Test 10: Withdraw from the opened account
    assert account.withdraw(800) == True  # Should succeed
    assert account.get_balance() == 1000  # Balance should reflect the withdrawal

    print("All tests passed!")

# Run the test cases
test_bank_account()