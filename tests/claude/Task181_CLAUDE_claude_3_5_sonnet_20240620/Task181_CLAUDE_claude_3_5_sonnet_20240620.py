from output.claude.Task181_CLAUDE_claude_3_5_sonnet_20240620 import *

def test_bank():
    bank = Bank()

    # Test 1: Open a new account
    assert bank.open_account("12345", 1000) == True

    # Test 2: Open the same account again (should fail)
    assert bank.open_account("12345") == False

    # Test 3: Deposit money into the account
    assert bank.deposit("12345", 500) == True

    # Test 4: Withdraw money from the account
    assert bank.withdraw("12345", 200) == True

    # Test 5: Withdraw more money than available (should fail)
    assert bank.withdraw("12345", 2000) == False

    # Test 6: Close the account
    assert bank.close_account("12345") == True

    # Test 7: Try to deposit into a closed account (should fail)
    assert bank.deposit("12345", 500) == False

    # Test 8: Try to withdraw from a closed account (should fail)
    assert bank.withdraw("12345", 200) == False

    # Test 9: Close the same account again (should fail)
    assert bank.close_account("12345") == False

    # Test 10: Try to open another account
    assert bank.open_account("67890", 1500) == True

    # Verify the balance after all transactions
    assert bank.accounts["67890"].balance == 1500

    print("All tests passed!")

# Run the test cases
test_bank()