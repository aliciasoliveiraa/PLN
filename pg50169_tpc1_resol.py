# Lesson 1 - Python Revision
from collections import Counter

# EXERCISES LESSON 1

# EXERCISE 1
# Programa que pergunta ao utilizador o nome e imprime em maiusculas.

name = input("What's your name? ")
name_user = name.upper()
print("My name is ", name_user)

# EXERCISE 2
# Funcao que recebe array de numeros e imprime os numeros pares.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def pares(numbers):
    for i in numbers:
        if i % 2 == 0:
            print("Par is ", str(i))

pares(numbers)

# EXERCISE 3
# Funcao que recebe nome do ficheiro e imprime linhas do ficheiro em ordem inversa.

file_name = input("What's the file name? ")
def print_reverse_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()
        r_lines = lines[::-1]
        for line in r_lines:
            print(line.strip())

print_reverse_lines(file_name)

# EXERCISE 4
# Funcao que recebe nome do ficheiro e imprime numero de ocorrencias das 10 palavras mais frequentes do ficheiro

import string

file_name2 = input("What's the file name? ")
def print_most_frequent_occurrences(file_name2):
    with open(file_name2, "r") as file2:
        text = file2.read()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    count_words = Counter(words)
    words_common = count_words.most_common(10)
    for word, count_word in words_common:
        print(f'{word}: {count_word}')

print_most_frequent_occurrences(file_name2)

# EXERCISE 5
# Funcao que recebe um texto como argumento e o limpa (separa palavras e pontuacao com espacos, converte
# para minusculas, remove a acentuacao de caracteres

import unicodedata
import string

text = input("What's the text? ")
def process_text(text):
    for c in string.punctuation + '“”‘’':
        text = text.replace(c, ' ')
    text = text.lower()
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII') # Remove accentuation
    text = ' '.join(text.split()) # Separate words and punctuation with spaces
    print("The clean text is: ", text)

process_text(text)

# CREATE A FUNCTION WITH OPERATIONS
text2 = input("What's the string? ")
def operations(text2):
    # Reverse string
    reverse_s = text2[::-1]
    print("Reverse string: ", reverse_s)

    # Count occ "a" and "A"
    count_all_a = text2.count("a") + text2.count("A")
    print("Count occ 'a' and 'A': ", count_all_a)

    # Count vowels
    count_vowels = sum(1 for c in text2 if c.lower() in 'aeiou')
    print("Count vowels: ", count_vowels)

    # Convert into lowercase
    lowercase_s = text2.lower()
    print("Convert into lowercase: ", lowercase_s)

    # Convert into upercase
    uppercase_s = text2.upper()
    print("Convert into upercase: ", uppercase_s)

operations(text2)