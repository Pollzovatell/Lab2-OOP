import unittest
from lab2 import Text

class TestText(unittest.TestCase):

    def test_init_valid_string(self):
        """Тест успішної ініціалізації з правильним типом даних"""
        text_obj = Text("Привіт, світ!")
        self.assertEqual(text_obj.text, "Привіт, світ!")

    def test_init_invalid_type(self):
        """Тест ініціалізації з неправильним типом даних"""
        with self.assertRaises(TypeError) as context:
            Text(12345)
        self.assertEqual(str(context.exception), "Помилка: Текст повинен бути рядком")

    def test_del_words_invalid_type(self):
        """Тест передачі неправильного типу для target_length"""
        text_obj = Text("Якийсь текст")
        with self.assertRaises(TypeError) as context:
            text_obj.del_words("3")
        self.assertEqual(str(context.exception), "Помилка: Довжина слова має бути цілим числом")

    def test_del_words_invalid_value(self):
        """Тест передачі недопустимого значення для target_length (<= 0)"""
        text_obj = Text("Якийсь текст")
        with self.assertRaises(ValueError) as context:
            text_obj.del_words(0)
        self.assertEqual(str(context.exception), "Помилка: Довжина слова має бути більшою за нуль")

        with self.assertRaises(ValueError):
            text_obj.del_words(-5)

    def test_del_words_normal_behavior(self):
        """Тест видалення слів заданої довжини, що починаються на приголосну"""
        text_obj = Text("На вулиці сонячно. Ми сьогодні гуляли в лісі. Кіт бігав")
        result = text_obj.del_words(3)
        expected = "На вулиці сонячно. Ми сьогодні гуляли в лісі. бігав"
        self.assertEqual(result, expected)

    def test_del_words_starts_with_vowel(self):
        """Тест перевірки того, що слова на голосну не видаляються, навіть якщо довжина збігається"""
        text_obj = Text("Око моє бачить усе")
        result = text_obj.del_words(3)
        self.assertEqual(result, "Око бачить усе")

    def test_del_words_with_punctuation(self):
        """Тест видалення слів разом із прилеглими розділовими знаками"""
        text_obj = Text("Дім, сад, ліс.")
        result = text_obj.del_words(3)
        self.assertEqual(result, "")

    def test_del_words_english_text(self):
        """Тест з англійським текстом для перевірки англійських голосних/приголосних"""
        text_obj = Text("The cat and dog are big")
        result = text_obj.del_words(3)
        self.assertEqual(result, "and are")

    def test_del_words_no_matching_words(self):
        """Тест, коли жодне слово не підпадає під критерії"""
        text_obj = Text("Тут немає слів з п'яти букв")
        result = text_obj.del_words(10)
        self.assertEqual(result, "Тут немає слів з п'яти букв")

    def test_del_words_empty_string(self):
        """Тест обробки порожнього рядка"""
        text_obj = Text("")
        result = text_obj.del_words(4)
        self.assertEqual(result, "")


if __name__ == '__main__':
    unittest.main()
