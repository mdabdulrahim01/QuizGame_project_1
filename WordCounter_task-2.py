# Function to count the number of words in the text
def count_words(text):
    if not text.strip():  # It Check if the input is empty or only contains whitespace
        return 0
    words = text.split()  # Now Splitting the text into words
    return len(words)  # Return the number of words

def main():
    # User input 
    user_input = input("Please enter a sentence or paragraph: ").strip()
    
    # Error handling for empty input
    if not user_input:
        print("Error: You entered an empty string. Please enter some text.")
    else:
        # Count the number of words
        word_count = count_words(user_input)
        
        # Display the word count
        print(f"The number of words in the input text is: {word_count}")

# Entry point of the program
if __name__ == "__main__":
    main()
