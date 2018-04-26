import subprocess
from http.server import HTTPServer, BaseHTTPRequestHandler
from unittest import TestCase
from swgohgg import SWGOHGG

httpd = None


class TestSWGOHGG(TestCase):
    """Tests for SWGOHGG class"""

    def setUp(self):
        """Sets up the mock server thread and sets up the """
        server_address = ('127.0.0.1', 0)
        httpd = HTTPServer(server_address, BaseHTTPRequestHandler)
        port = httpd.server_port
        httpd.server_close()

        url = 'http://127.0.0.1:{}/swgohgg_guild.html'.format(port)

        self.swgohgg_class = SWGOHGG
        self.swgohgg_class.swgoh_guild_url = url

        self.process = subprocess.Popen(['python', 'mock_server.py', '-port', str(port)])

    def tearDown(self):
        """Tears down the mock server thread"""
        self.process.kill()

    def test_init(self):
        """unit_tests initialization of SWGOHGG"""
        test_swgohgg = self.swgohgg_class()

        self.assertEqual(len(test_swgohgg.guild_response_soup.text), 5059)
        self.assertEqual(
            test_swgohgg.guild_response_soup.find('strong').text, 'Note'
        )

    def test_get_guild_gp(self):
        """unit_tests the SWGOHGG"""
        test_swgohgg = self.swgohgg_class()
        guild_gp = test_swgohgg.get_guild_gp()

        self.assertEqual(len(guild_gp), 48)
        self.assertIn('Krovikan', guild_gp)


