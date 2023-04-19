from heartbeat import BaseTest
import urllib.request
import urllib.error
import urllib.parse
import json
import nose.tools
import os
from nose.plugins.skip import SkipTest


class Test(BaseTest):
    def __init__(self, *args):
        self.proc = None
        super(Test, self).__init__(*args)

    def test_telemetry(self):
        """
        Test that telemetry metrics are correctly registered and increment / decrement
        """
        # This test is flaky https://github.com/elastic/beats/issues/8966
        raise SkipTest

    @staticmethod
    def assert_state(expected={}):
        stats = json.loads(urllib.request.urlopen(
            "http://localhost:5066/state").read())

        total_monitors = 0
        total_endpoints = 0

        for proto in ("http", "tcp", "icmp"):
            proto_expected = expected.get(proto, {})
            monitors = proto_expected.get("monitors", 0)
            endpoints = proto_expected.get("endpoints", 0)
            total_monitors += monitors
            total_endpoints += endpoints
            nose.tools.assert_dict_equal(stats['heartbeat'][proto], {
                'monitors': monitors,
                'endpoints': endpoints,
            })

        nose.tools.assert_equal(stats['heartbeat']['monitors'], total_monitors)
        nose.tools.assert_equal(
            stats['heartbeat']['endpoints'], total_endpoints)

    @staticmethod
    def assert_stats(expected={}):
        stats = json.loads(urllib.request.urlopen(
            "http://localhost:5066/stats").read())

        for proto in ("http", "tcp", "icmp"):
            proto_expected = expected.get(proto, {})
            nose.tools.assert_dict_equal(stats['heartbeat'][proto], {
                'monitor_starts': proto_expected.get("monitor_starts", 0),
                'monitor_stops': proto_expected.get("monitor_stops", 0),
                'endpoint_starts': proto_expected.get("endpoint_starts", 0),
                'endpoint_stops': proto_expected.get("endpoint_stops", 0),
            })
