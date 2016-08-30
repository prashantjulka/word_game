import random

def generate_random_word():
        words = ["Bvicam", "Python", "Java", "India"]
        return words[random.randint(0, len(words) - 1)]

def print_blank_word(word):
        for character in word:
                print(character, " ", end="")

def take_input():
        print("Enter character: ")
        return input()

def process(character, rand_word, blank_word):
        result = False
        for i in range(0, (len(rand_word))):
                if rand_word[i] == character:
                        result = True
                        blank_word[i] = character
        return result

def print_strikes(strikes):
    for i in range(0, strikes):
        print('X', end="")

def word_game():
        print("*******")
        strikes_count = 0
        max_strikes = 3
        finish = True
        blank_character = "_"
        rand_word = generate_random_word()
        blank_word = list(blank_character * len(rand_word))
        while finish:
                print_blank_word(blank_word)
                character = take_input()
                process_result = process(character, rand_word, blank_word)

                if not process_result:
                        strikes_count += 1
                        print_strikes(strikes_count)

                if max_strikes <= strikes_count:
                        finish = False

                if not "_" in blank_word:
                        finish = False

        if strikes_count >= max_strikes:
                print("Loser!")
        else:
                print(blank_word)
                print("Winner!")                      
print("****Game starts****")
word_game()
print("*****Game Over!*****")
                                                                                                                                                      
			