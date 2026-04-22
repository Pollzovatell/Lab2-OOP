class Text:
    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError("Помилка: Текст повинен бути рядком")

        self.text = text
        self.vowels = "аеєиіїоуюяaeiou"


    def del_words(self, target_length):
        if not isinstance(target_length, int):
            raise TypeError("Помилка: Довжина слова має бути цілим числом")

        if target_length <= 0:
            raise ValueError("Помилка: Довжина слова має бути більшою за нуль")

        try:
            words = self.text.split()
            result_words = []

            for word in words:
                clean_word = word.strip(".,!?:;")
                if not clean_word:
                    result_words.append(word)
                    continue

                first_letter = clean_word[0].lower()
                if (first_letter.isalpha() and first_letter not in self.vowels) and (len(clean_word) == target_length):
                    pass
                else:
                    result_words.append(word)

            return " ".join(result_words)

        except Exception as e:
            return f"Сталася внутрішня помилка при обробці тексту: {e}"


try:
    my_text = Text("На вулиці сонячно. Ми сьогодні гуляли в лісі. Кіт бігав")
    redacted_text = Text(my_text.del_words(3))

    print("Було:", my_text.text)
    print("Стало:", redacted_text.text)

except TypeError as error:
    print(error)
except ValueError as error:
    print(error)
except Exception as error:
    print(f"Критична помилка програми: {error}")
