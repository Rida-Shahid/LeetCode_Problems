class Solution:
    def sortSentence(self, s: str) -> str:
        
        # Split the shuffled sentence into words
        words = s.split()

        # Create a dictionary to store the words based on their positions
        word_dict = {}
        for word in words:
            position = int(word[-1])  # Extract the position from the word
            actual_word = word[:-1]   # Remove the position from the word
            word_dict[position] = actual_word

        # Reconstruct the original sentence by sorting the words based on their positions
        original_sentence = ' '.join(word_dict[i] for i in range(1, len(words) + 1))

        return original_sentence

    

        