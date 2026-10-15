word = "python"
guessed_letters = []

for letter in word:
    if letter in guessed_letters:
        print(letter, end=" ")
    else:
        print("_", end=" ")