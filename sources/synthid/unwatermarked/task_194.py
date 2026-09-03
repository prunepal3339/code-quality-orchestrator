# Definition for Master class.
class Master:
    def guess(self, word: str) -> int:
        pass

def findSecretWord(words: List[str], master: 'Master') -> None:
    while words:
        # Choose the word that maximizes the expected reduction of uncertainty
        best_word = max(words, key=lambda w: sum(master.guess(w) == i for i in range(7)))
        
        # Get the feedback from the master
        num_matches = master.guess(best_word)
        
        # Filter the list of words based on the feedback
        words = [w for w in words if sum(a == b for a, b in zip(w, best_word)) == num_matches]

# Example usage:
# master = Master()
# findSecretWord(["acckzz"], master)
