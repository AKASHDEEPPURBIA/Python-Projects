import csv

import requests #This module allows making HTTP requests.

from http import HTTPStatus
# This is an enumeration class in the http module
# that provides symbolic names for HTTP status codes.

from fake_useragent import UserAgent
# UserAgent: This is a class from the fake_useragent module that generates random user agent strings,
# often used to simulate different web browsers.

def get_websites(csv_path: str) -> list[str]:
    #loads websites from csv file
    websites: list[str] = []

    #This line of code opens the CSV file specified by csv_path in read mode ('r').
    # The with statement is used here, which ensures that the file is properly closed after its suite finishes,
    # even if an exception occurs during the execution.
    with open(csv_path,'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])

    return websites

def get_useragent() -> str:
    #this fun returns a user agent that can be used for requests

    ua = UserAgent()
    return ua.chrome

def get_status_description(status_code: int) -> str:
    # This function takes an HTTP status code as input
    # and returns a human-readable description of that status code.
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description

    return '(???) Unknow status code'

def check_websites(website: str, user_agent: str):
    # It sends an HTTP GET request to the specified website URL using the requests.get function.
    # It sets the user agent in the request headers to the provided user agent string.
    # It retrieves the HTTP status code from the response and
    # prints the website URL along with its description using the get_status_description function.
    # If an exception occurs during the request (e.g., network error),
    # it prints a message indicating that information for the website could not be retrieved.
    try:
        code: int = requests.get(website, headers = {'User_agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'**Could not get information for the website: {website}')

def main():
    sites: list[str] = get_websites('websites.csv')
    user_agent: str = get_useragent()

    for i, site in enumerate(sites):
        check_websites(site, user_agent)


if __name__ == '__main__':
    main()





