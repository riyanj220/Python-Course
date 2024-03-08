import random


# Function to encode a word
def encode(word):
    if len(word) < 3:
        # If the word has less than 3 characters, reverse it
        return word[::-1]
    else:
        # If the word has 3 or more characters, perform encoding
        first_letter = word[0]
        rest_of_word = word[1:]  # Remove the first character

        # Generate 3 random letters
        random_letters = "".join(
            random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(3)
        )

        # Construct the encoded word
        encoded_word = random_letters + rest_of_word + first_letter + random_letters
        return encoded_word


def decode(word):
    if len(word) < 3:
        # If the word has less than 3 characters, reverse it
        return word[::-1]
    else:
        # If the word has 3 or more characters, perform decoding
        first_three_letters = word[:3]
        middle_part = word[3:-3]  # Remove the first 3 and last 3 characters
        original_last_character = word[-3]

        # Construct the decoded word
        decoded_word = original_last_character + middle_part + first_three_letters
        return decoded_word


# Main program
while True:
    choice = input("Enter '1' to encode or '2' to decode (or 'q' to quit): ")

    if choice == "1":
        input_word = input("Enter the word to encode: ")
        encoded_word = encode(input_word)
        print(f"Encoded word: {encoded_word}")
    elif choice == "2":
        input_word = input("Enter the word to decode: ")
        decoded_word = decode(input_word)
        print(f"Decoded word: {decoded_word}")
    elif choice == "q":
        break
    else:
        print("Invalid choice. Please enter '1', '2', or 'q'.")
