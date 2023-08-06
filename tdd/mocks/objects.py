from datetime import datetime
import os
import requests
import time

SOME_CONSTANT = 3


def get_time_of_day():
    """return string Night/Morning/Afternoon/Evening depending on the hours range"""
    time = datetime.now()
    if 0 <= time.hour < 6:
        return "Night"
    if 6 <= time.hour < 12:
        return "Morning"
    if 12 <= time.hour < 18:
        return "Afternoon"
    return "Evening"


class DBConnector:
    def __init__(self):
        # Create a connection in theory
        pass

    def query(self):
        # Queries the db
        return "imaginary data"


class DBEngine:
    def __init__(self, connector):
        self.connector = connector

    def load_data(self):
        return self.connector.query()


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def monthly_schedule(self, month):
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return "Bad Response!"

    def get_department(self):
        return requests.get(f"http://company.com/{self.last}/{self.first}")


def get_environment():
    env = os.getenv("ENVIRONMENT")

    if env == "prod":
        return "prod-env"
    elif env == "dev":
        return "dev-env"
    raise ValueError("Unknown Environment")


def double_constant():
    return SOME_CONSTANT * 2
