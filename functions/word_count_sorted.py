def check_word_count(words):

    word_split = words.lower().split(" ")  # Generate individual words and store it in list
    word_split = [word.strip() for word in word_split if word.strip()]   # Added code to update list of words without whitespcaes
    word_frequency = {}

    for word in sorted(word_split) :
        if word not in word_frequency :
            word_frequency[word] = 1 
        else:
            word_frequency[word] = word_frequency[word] + 1 

    return(word_frequency)