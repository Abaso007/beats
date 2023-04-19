import os
from beat.beat import TestCase
from elasticsearch import Elasticsearch, NotFoundError


class BaseTest(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.beat_name = "mockbeat"
        cls.beat_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../")
        )
        cls.test_binary = f"{cls.beat_path}/libbeat.test"
        cls.beats = [
            "filebeat",
            "heartbeat",
            "metricbeat",
            "packetbeat",
            "winlogbeat",
        ]
        cls._es = None
        super(BaseTest, cls).setUpClass()

    def es_client(self):
        if self._es:
            return self._es

        self._es = Elasticsearch([self.get_elasticsearch_url()])
        return self._es
