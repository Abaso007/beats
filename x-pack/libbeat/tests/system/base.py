import sys
import os


sys.path.append(os.path.join(os.path.dirname(__file__),
                             '../../../../libbeat/tests/system'))


from beat.beat import TestCase


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.beat_name = "mockbeat"
        cls.beat_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../")
        )
        cls.test_binary = f"{cls.beat_path}/libbeat.test"
        super(BaseTest, cls).setUpClass()
