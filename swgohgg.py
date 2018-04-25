from bs4 import BeautifulSoup
from collections import OrderedDict
from urllib.request import Request, urlopen


class SWGOHGG():
    """A wrapper class to connect to and retrieve information from SWGOHGG

    Attributes:
         swgoh_guild_url (str): Guild's URL on SWGOH.GG, this needs to be changed before using the class.
         guild_response_soup (BeautifulSoup): Guild's SWGOH.GG downloaded into BeautifulSoup.
    """

    swgoh_guild_url = 'https://swgoh.gg/g/85/victory-march/'

    def __init__(self):
        guild_request = Request(self.swgoh_guild_url, headers={'User-Agent': "Python Browser"})
        guild_response = urlopen(guild_request)
        self.guild_response_soup = BeautifulSoup(guild_response, 'lxml')

    def get_guild_gp(self):
        """Scrapes the guild_response_soup to get a list of players and their current gp"""

        results = {}

        for player in self.guild_response_soup.find_all('tr'):
            name = player.find('strong')
            if name:
                name = name.text
            else:
                continue
            data = player.find_all('td')
            results[name] = data[1].text

        ordered_results = OrderedDict(sorted(results.items(), key=lambda x: x[0].lower()))

        return ordered_results
