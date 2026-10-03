# 🎮 Hangman Game (Python)

A simple command-line Hangman game written in Python. Guess the hidden word one letter at a time before you run out of lives!

## ✨ Features

- Random word selected from a built-in list of 100+ English words
- ASCII art that shows the hangman's progress
- 6 lives per game
- Detects letters you have already guessed
- Simple and beginner-friendly code

## 🛠️ Requirements

- Python 3.6 or higher

No external libraries are needed. The game only uses the built-in `random` module.

## 🚀 How to Run

1. Clone this repository or download the files:
```bash
   git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
```
2. Go to the project folder:
```bash
   cd YOUR-REPO-NAME
```
3. Run the game:
```bash
   python hangman.py
```

## 🕹️ How to Play

1. The game chooses a random word and shows it as underscores (`_ _ _ _`).
2. Type one letter and press Enter.
3. If the letter is in the word, it is revealed. If not, you lose a life and the hangman is drawn.
4. You win by guessing the whole word, and you lose when your lives reach 0.

## 📸 Example

```
_ _ _ _ _

Plz guess a letter :
a
_ _ _ a _
You have more 6 lives
```

## 📚 What I Learned

- Using lists and loops
- Working with `while` loops and conditions
- Taking user input
- Using the `random` module
- Formatting strings with f-strings

## 🔮 Future Improvements

- Add difficulty levels
- Validate input (accept only a single letter)
- Add a score system
- Load words from an external file

## 👤 Author

**Mehdi**
GitHub: [@ghezzaz-mehdi-dev](https://github.com/ghezzaz-mehdi-dev)
