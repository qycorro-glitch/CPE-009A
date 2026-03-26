def word_filter(sentence, bad_words):
    words = sentence.split()
    filtered_words = []

    for word in words:
        clean_word = word.strip('.,!?')  # handle punctuation
        if clean_word.lower() in bad_words:
            censored = '*' * len(clean_word)
            word = word.replace(clean_word, censored)
        filtered_words.append(word)

    return ' '.join(filtered_words)


# Example usage
sentence = "This is a bad example with ugly words."
bad_words = ["bad", "ugly"]

print(word_filter(sentence, bad_words))