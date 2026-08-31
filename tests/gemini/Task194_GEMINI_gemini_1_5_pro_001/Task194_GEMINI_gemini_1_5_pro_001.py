# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:
from typing import List

class Solution:
    def findSecretWord(self, words: List[str], master: 'Master') -> None:
        n = len(words)
        self.H = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                matches = sum(words[i][k] == words[j][k] for k in range(6))
                self.H[i][j] = self.H[j][i] = matches

        possible = list(range(n))
        matches = 0
        while matches < 6:
            guess = self.findBestGuess(possible)
            matches = master.guess(words[guess])
            if matches == 6: break
            possible = [j for j in possible if self.H[guess][j] == matches]

    def findBestGuess(self, possible):
        mx = len(possible)
        ans = -1
        for i in possible:
            groups = [0] * 7
            for j in possible:
                if i != j:
                    groups[self.H[i][j]] += 1
            mx_group = max(groups)
            if mx_group < mx:
                mx = mx_group
                ans = i
        return ans