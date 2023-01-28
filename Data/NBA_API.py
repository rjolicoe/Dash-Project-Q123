import keyring
import requests

class NBA_Data_Retrieval:

    def __init__(self, season = 2022, url = "https://free-nba.p.rapidapi.com/players",
                servicename = "X-RapidAPI-Host",
                username = "X-RapidAPI-Key",
                host_url = "free-nba.p.rapidapi.com",
                querystring = {"page":"0","per_page":"25"}):
        self.season = season
        self.url = url
        self.servicename = servicename
        self.username = username
        self.api_key = keyring.get_password(servicename, username)
        self.host_url = host_url
        self.querystring = querystring

    def retrieve_data(self):
        """

        :return: Response from API
        """
        # print(self.username)
        headers = {
            self.username: self.api_key,
            self.servicename: self.host_url
        }

        self.headers = headers

        response = requests.request("GET", url=self.url,
                                    headers=headers,
                                    params=self.querystring)

        return response

if __name__ == '__main__':
    NBAR = NBA_Data_Retrieval()

    response = NBAR.retrieve_data()

    print(type(response.text))