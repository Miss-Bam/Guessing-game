import random

food = ["melon","guava","pecan","pasta","steak","donut","bagel","cream","pizza"]
transport = ["buses","carts","ships","taxis","truck","rides"]
sport = ["boxer","field","lunge","score","racer","coach"]
animals = ["whale", "tiger", "goose", "zebra"]
nature = ["river", "earth", "beach", "grass"]
home = ["house", "chair", "table", "light"]
clothing = ["shirt", "dress", "shoes"]
emotions = ["happy", "angry", "brave", "faint"]
weather = ["storm", "cloud"]
body = ["heart", "brain", "teeth"]

categories = {"food":food, "transport":transport, "sport": sport, "animals":animals, "nature":nature, 
              "home":home, "clothing":clothing, "emotions": emotions, "weather":weather, "body":body}

topics = ["food","transport","sport","animals","nature","home","clothing","emotions","weather","body"]


"""How the pointing system works:
    1. Get 50 points for guessing the correct word.
    2. Get 10 points for each correctly guessed letter in the right position
    3. Get 5 points for each correctly guessed letter in the wrong position
"""

"""Display: 
    1. Correct word: A B C D E
    2. Incorrect word: f g h i j
    3. Correct letters: A g b* i E
    Capitalized letters for correct placement,
    small letters for incorrect letters and 
    letters with * for incorrectly positioned correct letters
"""

def inputValidator(userGuess):
    if len(userGuess) == 5 and userGuess.isalpha():
        return True
    
    else:
        return False
    
    
def generateResult(correctWord, userGuess):
    pointsObtained = 0
    output = "| "
    for i in range(5):
        if userGuess[i] == correctWord[i]:
            output += userGuess[i].upper() + " | "
            pointsObtained += 10

        elif userGuess[i] in correctWord:
            output += userGuess[i]+"* | "
            pointsObtained += 5

        else:
            output += userGuess[i] + " | "


    return (output, pointsObtained)


def generateOutput(results):
    print("Word : "+results[0])
    print("Points obtained: "+str(results[1]))

def guessPrompt():
    while True:
            userGuess = input("Enter your guess: ").lower()
            if inputValidator(userGuess):
                return userGuess
            print("ERROR! Your guess should only be a 5 letter word. No numbers or special characters!")

def playAgain():
    userInput = input("Enter YES to play again or NO to quit the game: ").lower()
    if userInput == "yes":
        return True
    
    elif userInput == "no":
        return False
    
    else:
        playAgain()


def play():
    
    playing = True
    
    while playing:
        category = random.choice(topics)
        categoryList = categories[category]
        correctWord = random.choice(categoryList)
        print("The topic for this category is : "+category+".\nYou have 3 chances to guess the word.")
        
        for i in range(3):
            print()
            userGuess = guessPrompt()
            if userGuess == correctWord:
                results = generateResult(correctWord, userGuess)
                generateOutput(results)
                print()
                print("Congratulations! You have won the game!!!")
                print()
                break

            else:
                results = generateResult(correctWord,userGuess)
                generateOutput(results)
                print()
                print("You have "+str(2-i)+" guesses remaining.")
                print()

        
        playing = playAgain()
        print()


play()





        
        

        
        
        
        
        