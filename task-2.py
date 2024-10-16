# Задание 2: Подсчет гласных и согласных букв
word = input("Введите слово из маленьких латинских букв: ").lower()
vowels = 'aeiou'
consonants = 0
vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for char in word:
    if char in vowels:
        vowel_count[char] += 1
    elif char.isalpha():
        consonants += 1

# Проверяем наличие всех гласных
all_vowels_present = all(vowel_count[char] > 0 for char in vowels)

# Выводим количество гласных и согласных
print(f"Согласных букв: {consonants}")
print(f"Гласных букв: {sum(vowel_count.values())}")
print(f"Количество каждой гласной: {vowel_count}")

# Выводим True или False в зависимости от наличия всех гласных
print(all_vowels_present)
