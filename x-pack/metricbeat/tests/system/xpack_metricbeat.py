import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../metricbeat/tests/system'))

import metricbeat


class XPackTest(metricbeat.BaseTest):

    @classmethod
    def setUpClass(cls):
        cls.beat_name = "metricbeat"
        cls.beat_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../../")
        )

        cls.template_paths = [
            os.path.abspath(os.path.join(cls.beat_path, "../../metricbeat")),
            os.path.abspath(os.path.join(cls.beat_path, "../../libbeat")),
        ]

        super(XPackTest, cls).setUpClass()

    def setUp(self):
        super(XPackTest, self).setUp()
