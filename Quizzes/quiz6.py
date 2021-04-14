import sys
import james

# credit to James for quiz 5 code


def get_question_bank(fileName: str):
    '''
    parses txt files for properly formatted
    '''
    try:
        questions = open(fileName)
    except FileNotFoundError:
        print("File not found, check file is in same directory")
        sys.exit()

    lines = questions.readlines()
    totalLines = len(lines)
    blankLines = 0

    cleaned = []
    for line in lines:
        insert = line.strip().split()
        if len(insert) == 6:
            cleaned.append(insert)
        if line == '\n':
            blankLines += 1

    for idx, question in enumerate(cleaned):
        for word in question:
            if not word.isalpha():
                cleaned.remove(cleaned[idx])

    while cleaned.__contains__([]):
        cleaned.remove([])

    return [cleaned, totalLines, blankLines]


def display(questions: list, answers: list, total, blank):
    '''
    main display of program, takes the questions and answers lists as given
    from main() and the total and blank line counts from get_questions_banks()
    '''
    print("-" * 57)
    print("Welcome to the Synonym Question Program by Charlie Taylor")
    print("-" * 57)

    for idx in range(len(questions)):
        print("Test question word: ", questions[idx][0])
        print("Computer answer:", answers[idx],
              "Test answer:", questions[idx][-1], '\n')

    print("Total lines in file: ", total)
    print("Total questions processed:", total - blank)
    print("Total skipped lines:", blank)


def get_vectors(fileName: str) -> dict:
    '''
    gets word vectors from specified file and returns dict of dicts
    '''
    try:
        text = open(fileName)
        return james.get_word_vectors(james.get_sentences(text.read()))
    except FileNotFoundError:
        print("File not found, check file is in same directory")
        sys.exit()


def find_most_similar(questions: list, vectors: dict):
    '''
    takes questions from get_question_bank() and vectors from get_vectors()
    and determines what word has the highest cosine similarity to the
    test word
    '''
    answers = []
    for idx in range(len(questions)):
        previous = 0
        mostSimilar = ''
        for q in range(1, 5):
            testWord = questions[idx][0]
            compare = questions[idx][q]
            score = james.cosine_simularity(vectors.get(testWord),
                                            vectors.get(compare))
            if score > previous:
                mostSimilar = compare
            previous = score
        answers.append(mostSimilar)
    return answers


def main(args):
    vectors = get_vectors(args[1])
    questions = get_question_bank(args[2])
    questions, total, blank = questions[0], questions[1], questions[2]
    answers = find_most_similar(questions, vectors)
    display(questions, answers, total, blank)


if __name__ == "__main__":
    main(sys.argv)
