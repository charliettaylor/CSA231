import math
import pprint as pp


def get_sentences(line):
    sentences = []
    last = 0
    for idx, char in enumerate(line):
        if char in '.?!':
            sentences.append(line[last:idx])
            last = idx

    remove = [',', ',', '--', ':', ';', '.', '?', '!']
    for idx in range(len(sentences)):
        for punc in remove:
            sentences[idx] = sentences[idx].replace(punc, '')
        sentences[idx] = sentences[idx].strip().lower().split()
    
    return sentences


def get_word_vectors(sentences):
    allWords = set()
    for sen in sentences:
        for word in sen:
            if word not in allWords:
                allWords.add(word)

    wordVectors = {}

    for word in allWords:
        wordVectors[word] = {}
        for sen in sentences:
            if word in sen:
                for each in sen:
                    if each != word:
                        if word not in wordVectors[word]:
                            wordVectors[word][each] = 1
                        else:
                            wordVectors[word][each] += 1
    return wordVectors


def main():
    print("Welcome to the Cosine Similarity Test! By Charlie Taylor")
    text = input("Enter a passage of text")
    word1 = input('Enter a word: ').lower()
    word2 = input('Enter a word: ').lower()
    word3 = input('Enter a word: ').lower()
    while not(word1 in text and word2 in text and word3 in text):
        text = input("Enter a valid passage of text")
        word1 = input('Enter a word: ').lower()
        word2 = input('Enter a word: ').lower()
        word3 = input('Enter a word: ').lower()
    sentences = get_sentences(text)
    vectors = get_word_vectors(sentences)
    w1 = vectors[word1]
    w2 = vectors[word2]
    w3 = vectors[word3]

    print("Word 1 and 2 have similarity", cosine_similarity(w1, w2))
    print("Word 1 and 3 have similarity", cosine_similarity(w1, w3))


def testing():
    test = 'I am a sick man. I am a spiteful man. I am an unattractive man.'

    sent = get_sentences(test)
    assert sent == list
    vectors = get_word_vectors(sent)
    assert vectors == dict
    cs = cosine_similarity({'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6})
    assert cs == float


def cosine_similarity(v1, v2):
    """
    Takes two word vectors (as returned by get_word_vectors).
    Returns their similarity score as a float.

    Example:
        cosine_similarity({'a': 1, 'b': 2, 'c': 3}, {'b': 4, 'c': 5, 'd': 6}) -> ~.70
    """
    # Cosine Sim:
    # Get the words that both have in common

    v1words = set(v1.keys())
    v2words = set(v2.keys())

    numerator_words = v1words.intersection(v2words)

    # Multiply and sum those counts
    numerator = 0.0
    for word in numerator_words:
        numerator += v1[word] * v2[word]


    # Divide by the sqrt of the product of the sum of the squares of the counts
    denominator = math.sqrt(math.magnitude(list(v1.values())) * math.magnitude(list(v2.values())))

    return numerator/denominator


if __name__ == "__main__":
    main()