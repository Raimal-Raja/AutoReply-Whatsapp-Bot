import unittest
from chat_utils import is_last_message_from_sender

class TranscriptTests(unittest.TestCase):
    def test_current_year_and_multiline_message(self):
        self.assertTrue(is_last_message_from_sender('[14:34, 8/10/2026] Thy Professor Gb: Hello\nMore text'))

    def test_sender_mentioned_in_another_persons_message(self):
        self.assertFalse(is_last_message_from_sender('[14:34, 8/10/2026] Other: Thy Professor Gb said hello'))

    def test_latest_sender_and_empty_transcript(self):
        self.assertFalse(is_last_message_from_sender('[14:34, 8/10/2026] Thy Professor Gb: Hi\n[14:35, 8/10/2026] Other: Reply'))
        self.assertFalse(is_last_message_from_sender(''))

if __name__ == '__main__':
    unittest.main()
