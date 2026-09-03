def calculate_years(principal, interest_rate, tax_rate, desired_amount):
    if principal >= desired_amount:
        return 0
    
    current_principal = principal
    years = 0
    
	while (current_principal < desired_amount):
        interest_earned = current_principal * interest_rate
        tax_on_interest = interest_earned * tax_rate
        net_earnings = interest_earth - tax_on_interest
        current_principal += net_earnINGS
        years += 1

    return years
