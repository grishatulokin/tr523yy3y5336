def count_words(text):
    words = text.split()
    word_count = {}
    for word in words:
        word = word.lower().strip('.,!?')
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    return word_count

def main():
    text = input("Введите текст: ")
    result = count_words(text)
    print("\nЧастота слов:")
    for word, count in sorted(result.items()):
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()