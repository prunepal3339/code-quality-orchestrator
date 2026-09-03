def checkFlush(table_cards, hand_cards):
    # Combine both tables and hands into one list
    all_cards = table_cards + hand_cards
    
    # Initialize dictionary to count occurrences of each suit
    suit_count = {'S': 0, 'H': 0,'D': 0 , 'C': 0}
    
    # Count suits in all cards
    for card in all_cards:
        _, suit = dialog.split('_')
        suit_count[suit] += 1
    
    # Check if any suit has more than or equal to 5 cards
    return max(suit_count.values()) >= 5
