import requests
from prettytable import PrettyTable
import logging


class CountryInfo:
    def __init__(self, api_url: str = "https://restcountries.com/v3.1/all"):
        self.api_url = api_url
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def fetch_data(self):
        params = {
            'fields': 'name,capital,flags'  # Запрашиваем только нужные поля
        }
        try:
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"Error fetching data from API: {e}")
            return []

    def display_data(self):
        data = self.fetch_data()
        if not data:
            self.logger.error("No data available to display.")
            return

        table = PrettyTable()
        table.field_names = ["Country", "Capital", "Flag URL (PNG)"]

        for country in data:
            name = country.get("name", {}).get("common", "N/A")
            capital = country.get("capital", ["N/A"])
            capital_name = capital[0] if capital else "N/A"
            flag_url = country.get("flags", {}).get("png", "N/A")
            table.add_row([name, capital_name, flag_url])

        print(table)

if __name__ == "__main__":
    ci = CountryInfo()
    ci.display_data()
