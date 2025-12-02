"""hangman.py
Hangman with:
- Built‑in word list (no external files)
- Meaning hint visible
- Continuous play (auto next word until user exits)
- Fill‑in‑the‑blanks start
"""    

import random

def load_words():
    return [
        ("python","A popular high-level programming language."),
        ("variable","A named storage location for values in a program."),
        ("function","A reusable block of code that performs a specific task."),
        ("algorithm","A step-by-step procedure to solve a problem."),
        ("compiler","A program that converts source code into machine code."),
        ("debugger","A tool used to test and debug programs."),
        ("database","An organized collection of structured information or data."),
        ("internet","A global network that connects computers."),
        ("laptop","A portable personal computer."),
        ("keyboard","An input device used to type text."),
        ("software","Programs used by a computer."),
        ("hardware","Physical parts of a computer."),
        ("developer","A person who writes code."),
        ("programming","Process of writing computer programs."),
        ("repository","A storage location for code."),
        ("github","A platform for hosting code."),
        ("college","An educational institution."),
        ("student","A person studying."),
        ("semester","A half-year term."),
        ("library","A place with books for studying."),
        ("assignment","A task given to students."),
        ("project","A planned piece of work."),
        ("holiday","A day of celebration and rest."),
        ("mountain","A large natural elevation."),
        ("festival","A celebration event."),
        ("language","A system of communication."),
        ("music","Art of sound."),
        ("guitar","A stringed musical instrument."),
        ("cricket","A popular bat-and-ball sport.")
    ]

def choose_word(words):
    w,h = random.choice(words)
    return w.upper(),h

def display(secret, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in secret)

def print_hangman(tries):
    stages=[
        """
         _______
        |/      |
        |      (_)
        |      /|\\
        |       |
        |      / \\
        |
        |___
        """, """
         _______
        |/      |
        |      (_)
        |      /|\\
        |       |
        |      / 
        |
        |___
        """, """
         _______
        |/      |
        |      (_)
        |      /|\\
        |       |
        |      
        |
        |___
        """, """
         _______
        |/      |
        |      (_)
        |      /|
        |       |
        |      
        |
        |___
        """, """
         _______
        |/      |
        |      (_)
        |       |
        |       |
        |      
        |
        |___
        """, """
         _______
        |/      |
        |      (_)
        |      
        |      
        |      
        |
        |___
        """, """
         _______
        |/      |
        |      
        |      
        |      
        |      
        |
        |___
        """
    ]
    idx = max(0,min(6,6-tries))
    print(stages[idx])

def init_reveal(secret):
    unique=list(set(secret))
    count=max(1,len(unique)//3)
    return set(random.sample(unique,count))

def play_one_round(words):
    secret,hint=choose_word(words)
    guessed=init_reveal(secret)
    wrong=set()
    tries=6

    print(f"\nHint: {hint}\n")

    while True:
        print_hangman(tries)
        print("Word:",display(secret,guessed))
        print("Wrong guesses:",", ".join(sorted(wrong)) or "-")
        print(f"Tries left: {tries}")
        print("-"*40)

        g=input("Enter a letter: ").upper().strip()
        if len(g)!=1 or not g.isalpha():
            print("Invalid input.\n")
            continue
        if g in guessed or g in wrong:
            print("Already guessed.\n")
            continue

        if g in secret:
            guessed.add(g)
            print(f"Good job! '{g}' is in the word.\n")
        else:
            wrong.add(g)
            tries-=1
            print(f"'{g}' is not in the word.\n")

        if display(secret,guessed).replace(" ","")==secret:
            print_hangman(tries)
            print(f"YOU WON! Word was: {secret}\n")
            break

        if tries<=0:
            print_hangman(tries)
            print(f"YOU LOST! Word was: {secret}\n")
            break

def main():
    words=load_words()
    print("="*40)
    print("          HANGMAN GAME")
    print("="*40)

    while True:
        play_one_round(words)
        ch=input("Play again? (y/n): ").lower().strip()
        if ch!='y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
