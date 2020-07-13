"""
tests evaluation of input
"""
import sys
import unittest
sys.path.append('..')
sys.path.append('.')


class TestInput(unittest.TestCase):
    """
    Test coherence of parser
    """
    def test_some_questions(self):
        """
        Is filtering is operational ?
        """
        from gpapp import Question
        # Basic test
        str_question = "question"
        question = Question(str_question)
        some_answer = question.get_shortened_question()
        another_answer = question.get_whole_question()
        self.assertEqual(another_answer, some_answer)

        # test filter
        str_question = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
        question = Question(str_question)
        shortened_question = question.get_shortened_question()
        self.assertEqual(shortened_question, "openclassrooms")


if __name__ == '__main__':
    unittest.main()
