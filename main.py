from functions.word_count_sorted import check_word_count

def main():
    
    sentence = "which is better python 2 or Python 3"
    result = check_word_count(sentence)
    print(result)

    # Sending inputs from file to run some test scenarios
    with open("test_inputs/inputs.txt", "r") as file:
        sentence = file.readlines()
    
    for words in sentence:
        print(f" {words} {check_word_count(words)}")



if __name__ == "__main__":
    main()