from unittest import TestCase
from numpy import array as nparray
from youtube_sentiment import flatten_list
from youtube_sentiment import load_ml_pipeline
from youtube_sentiment import top_freq_words
from youtube_sentiment import total_counts
from youtube_sentiment import extract_entities

class TestUtil(TestCase):
    """ Test Utility """
    @classmethod
    def setUpClass(self):
        """ Setup """

    """ Utility class tests """
    def test_flatten_list(self):
        """ Test flatten list of lists structure """
        mock = [["Was a great movie"], ["Wow did you see that?"]]
        self.assertTrue(flatten_list(mock) == ["Was a great movie", "Wow did you see that?"])

    def test_load_model(self):
        """ Test loading of a model """
        mock = load_ml_pipeline("lr_sentiment_basic.pkl")
        self.assertTrue(mock != None)
        self.assertTrue(hasattr(mock, 'predict'))
        with self.assertRaises(Exception) as mockexception:
            r = load_ml_pipeline("lr_sentiment_findme.pkl")

    def test_model_predict(self):
        """ Test model sentiment predict and action """
        mock_comments = ["Hey nice video you made loved it", "Terrible video worst ever"]
        mock = load_ml_pipeline("lr_sentiment_basic.pkl")
        predictions = mock.predict(mock_comments)
        self.assertTrue(predictions[0] == 1)
        self.assertTrue(predictions[1] == 0)

    def test_comments_frequency(self):
        """ Test comments word frequencies """
        mock_comments = "Hey nice video you made loved it Terrible video worst ever loved it loved"
        top_words = top_freq_words(mock_comments, topwords=20)
        self.assertTrue(len(top_words) > 1)
        self.assertTrue(top_words[0] == ("loved", 3))

    def test_arr_counts(self):
        """ Test numpy counts of values """
        mock_counts = nparray([0, 0, 1, 1, 1])
        counts = total_counts(mock_counts)
        self.assertTrue(counts == (3, 2))

    def test_extract_entities(self):
        """ Test entity extract via NLTK """
        mock_comments = "Hey nice video you made loved it Mike is in Japan right now good job"
        entities = extract_entities(mock_comments)
        self.assertTrue(len(entities) > 0)
        self.assertTrue("Mike" in entities)