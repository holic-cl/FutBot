#!/usr/bin/python
import requests
from bs4 import BeautifulSoup
import unicodedata


class ScotiabankTournament:
    """
    Basic http scraper to fetch information about Chilean Football
    championship.
    """

    base_url = 'http://anfp.cl'

    def get_statistics(self):
        """
        Fetch tournament statistics from
        http://anfp.cl/estadisticas/scotiabank.
        """
        req = self.get(self.base_url + '/estadisticas/scotiabank')
        soup = BeautifulSoup(req.text, 'html.parser')
        table = soup.find('table', attrs={'id': 'datatable-responsive'})
        table_headers = table.find('thead').find_all('tr')
        table_headers = table_headers[0].find_all('th')
        table_headers = [el.text.strip() for el in table_headers]
        table_body = table.find('tbody')
        rows = table_body.find_all('tr')

        teams = []
        for row in rows:
            cols = row.find_all('td')
            cols = {
                table_headers[i]: el.text.strip() for i, el in enumerate(cols)
            }
            teams.append(cols)
        return teams

    def get_schedule(self, schedule):
        """
        Fetch information about the tournament schedule.
        Info is taken from:
        http://anfp.cl/vital-programacion/petrobas/{schedule}.
        Schedule is the schedule of the tournament. Valids only 1 to 15.
        """
        if (schedule < 0 and schedule > 15):
            raise ValueError('The schedule is not valid.')
        req = self.get(self.get_schedule_url(schedule))
        soup = BeautifulSoup(req.text, 'html.parser')
        matches_list = soup.find('ul', attrs={'class': 'info-fechas'})
        matches_list = matches_list.find_all('li')

        matches = []
        for row in matches_list:
            divs = row.find_all('div')
            matches.append({
                'schedule': divs[0].text,
                'local': divs[1].find('span', attrs={'class': 'local'}).text,
                'visit': divs[1].find('span', attrs={'class': 'visita'}).text,
                'stadium': divs[2].find(
                    'span', attrs={'class': 'estadio'}
                ).text
            })
        return matches

    def print_statistics(self):
        print(self.get_statistics())

    def print_schedule(self, schedule):
        print(self.get_schedule(schedule))

    def get(self, url):
        user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) '
        user_agent += 'AppleWebKit/537.36 (KHTML, like Gecko) '
        user_agent += 'Chrome/50.0.2661.102 Safari/537.36'

        return requests.get(url, headers={
            'User-Agent': user_agent
        })

    def get_schedule_url(self, schedule):
        return self.base_url + '/vital-programacion/petrobas/' + str(schedule)

    def decodeText(text):
        return unicodedata.normalize('NFD', text).encode('ascii', 'ignore')
