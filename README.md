# Project Description

This project demonstrates interacting with an API to fetch country information and displaying it in a tabular format.

## Dependencies

To run the project, you can install the required dependencies listed in `requirements.txt`. This includes:

- `requests`: for making HTTP requests to the API
- `prettytable`: for creating visually appealing tables when displaying data

## Installation

You can install the dependencies using `pip` and the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This command will install the specific versions of `requests` and `prettytable` as listed in `requirements.txt`.

## Usage

The project includes the `CountryInfo` class, which retrieves country data from the `https://restcountries.com/v3.1/all` API, extracts relevant information (country name, capital, and URL to the flag image in PNG format), and displays it in the console as a table.

Usage example:

```bash
python main.py
```

Running this command will execute the script and display country data in a tabular format.
