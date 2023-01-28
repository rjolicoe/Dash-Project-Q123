import keyring

if __name__ == '__main__':
    keyring.set_password("X-RapidAPI-Host", "X-RapidAPI-Key",
                         "020f2b0544mshb231f7939bd760fp171d50jsnca2dce7a9b39")

    api_key = keyring.get_password("X-RapidAPI-Host", "X-RapidAPI-Key")