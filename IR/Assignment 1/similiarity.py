import math
import string
import sys

def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except IOError:
        print(f"Error opening or reading input file: {file_path}")
        sys.exit()

# Create a translation table to replace punctuation with spaces and convert uppercase to lowercase
translation_table = str.maketrans(
    string.punctuation + string.ascii_uppercase,
    " " * len(string.punctuation) + string.ascii_lowercase
)

def extract_words(text):
    """Converts the text to lowercase and removes punctuation, returning a list of words."""
    clean_text = text.translate(translation_table)
    words = clean_text.split()
    return words

def count_word_frequencies(words):
    """Counts the frequency of each word in the list."""
    frequency_dict = {}
    for word in words:
        frequency_dict[word] = frequency_dict.get(word, 0) + 1
    return frequency_dict

def calculate_word_frequencies(file_path):
    """Processes the file and returns a frequency dictionary of words in the file."""
    content = read_file(file_path)
    words = extract_words(content)
    frequencies = count_word_frequencies(words)

    print(f"File {file_path}:")
    print(f"{len(content)} characters,")
    print(f"{len(words)} words,")
    print(f"{len(frequencies)} distinct words")
    print("--------------------------------------------------------")
    return frequencies

def calculate_dot_product(freq_dict1, freq_dict2):
    """Calculates the dot product between two frequency dictionaries."""
    dot_product_sum = sum(freq_dict1[word] * freq_dict2.get(word, 0) for word in freq_dict1)
    return dot_product_sum

def calculate_vector_angle(freq_dict1, freq_dict2):
    """Calculates the angle between two word frequency vectors."""
    numerator = calculate_dot_product(freq_dict1, freq_dict2)
    denominator = math.sqrt(calculate_dot_product(freq_dict1, freq_dict1) * calculate_dot_product(freq_dict2, freq_dict2))
    
    if denominator == 0:
        return math.pi / 2  # Return 90 degrees if one document has no words
    return math.acos(numerator / denominator)

def document_similarity(file_path1, file_path2):
    """Computes the similarity between two documents and prints the angular distance."""
    freq_dict1 = calculate_word_frequencies(file_path1)
    freq_dict2 = calculate_word_frequencies(file_path2)
    angle = calculate_vector_angle(freq_dict1, freq_dict2)
    print(f"The distance between the documents is: {angle:.6f} radians")

# Compare the similarity between two documents
print("--------------------------------------------------------")
document_similarity('./sample1.txt', './sample2.txt')
print("--------------------------------------------------------")
