# Word Count App

Hey there! This is a simple Python app that counts how many times each word appears in a given text. 

## Files

Here's a quick overview of what you'll find in this project:

- main.py: This is where everything starts. It shows how to use the `check_word_count` function with a sample sentence and also reads some test sentences from a file.

- functions/:
  - word_count_sorted.py: This file has the `check_word_count` function. It splits a sentence into words, cleans up any extra spaces, and counts how often each word shows up. The results come back as a nice sorted dictionary.

- test_word_count.py: This is a collection of tests using Pytest for the `check_word_count` function. It checks for different cases like:
  - Empty strings
  - Single words
  - Repeated words
  - Mixed cases
  - Special characters
  - And more!

- test_inputs/:
  - inputs.txt: A text file with various sentences to test the function. It includes different cases, punctuation, and numbers.

## Requirements
  - Python
  - Pytest


## How to Use

1. Clone this repo:
   git clone <https://github.com/codewithshubham/pre-int-screening.git>
2. Run the main app:
   python main.py
3. Run pytest :
   pytest test_word_count.py

