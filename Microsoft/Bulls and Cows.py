from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l = len(guess)
        s = Counter(secret)
        x = 0 
        y = 0 
        
        for i in range(l):
            if guess[i] == secret[i]:
                x += 1
                s[guess[i]] -= 1

        for i in range(l):
            if guess[i] != secret[i] and s[guess[i]] > 0:
                y += 1
                s[guess[i]] -= 1
                
        return f"{x}A{y}B"
