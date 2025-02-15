class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = {}  # Dictionary to store character frequencies

        # Count frequency of each character
        for char in word:
            freq[char] = freq.get(char, 0) + 1

        # Try removing one occurrence of each character and check if the remaining frequencies are equal
        for char in set(word):
            temp_freq = freq.copy()  # Make a copy of the frequency dictionary
            temp_freq[char] -= 1

            if temp_freq[char] == 0:
                del temp_freq[char]  # Remove key if its value becomes zero

            values = list(temp_freq.values())  # Get remaining frequencies

            if len(set(values)) == 1:  # Check if all values are the same
                return True

        return False