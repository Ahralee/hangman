"""Unit test cases for hangman game."""
import unittest
import hangman

class HangmanTestCase(unittest.TestCase):

    # checkCorrectAnswer(correctLetters, secretWord)
    def test_checkCorrectAnswer(self):
        answer = hangman.checkCorrectAnswer("baon", "baboon")
        self.assertTrue(answer)

        answer = hangman.checkCorrectAnswer("osega", "goose")
        self.assertTrue(answer)

        answer = hangman.checkCorrectAnswer("", "goose")
        self.assertFalse(answer)

        answer = hangman.checkCorrectAnswer("abcndkekjasd", "")
        self.assertTrue(answer)

        answer = hangman.checkCorrectAnswer("", "")
        self.assertTrue(answer)

    def test_checkWrongAnswer(self):
        answer = hangman.checkWrongAnswer("zebrio", "zebra")
        self.assertTrue(answer)

        answer = hangman.checkWrongAnswer("elegae", "elephant")
        self.assertTrue(answer)

        answer = hangman.checkWrongAnswer("frolifca", "frog")
        self.assertFalse(answer)

if __name__ == "__main__":
    unittest.main()
