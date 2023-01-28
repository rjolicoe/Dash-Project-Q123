import keyring
import pandas as pd
import requests

class NBA_Data_Retrieval():

    def __init__(self, season=2022, url="https://free-nba.p.rapidapi.com/players",
                 servicename="X-RapidAPI-Host",
                 username="X-RapidAPI-Key",
                 host_url="free-nba.p.rapidapi.com",
                 querystring={"page": "0", "per_page": "25"}):
        self.season = season
        self.url = url
        self.servicename = servicename
        self.username = username
        self.api_key = keyring.get_password(servicename, username)
        self.host_url = host_url
        self.querystring = querystring

    def retrieve_data(self):
        """

        :return: Request response from the API and convert into
                 pandas dataframe
        """
        headers = {
            self.username: self.api_key,
            self.servicename: self.host_url
        }
        self.headers = headers
        response = requests.request("GET", url=self.url,
                                    headers=headers,
                                    params=self.querystring)
        df = response.json()
        df2 = pd.json_normalize(df, sep="_")

        vals = df2.data
        nba_df = pd.json_normalize(vals[0])

        return nba_df





