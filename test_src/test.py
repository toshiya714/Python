from random import random
from re import M
import hangman
import random

wordlist = ["cat", "morning", "spring", "summer", "winter", "autumn"]
word = random.choice(wordlist)

hangman.hangman(word)