import requests
from prettytable import PrettyTable

class CountryInfo:
    def __init__(self, api_url="https://restcountries.com/v3.1/all"):
        self.api_url = api_url

    def fetch_data(self):
        response = requests.get(self.api_url)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def display_data(self):
        data = self.fetch_data()
        table = PrettyTable()
        table.field_names = ["Country", "Capital", "Flag URL (PNG)"]

        for country in data:
            name = country.get("name", {}).get("common", "N/A")
            capital = country.get("capital", ["N/A"])[0]
            flag_url = country.get("flags", {}).get("png", "N/A")
            table.add_row([name, capital, flag_url])

        print(table)

if __name__ == "__main__":
    ci = CountryInfo()
    ci.display_data()
