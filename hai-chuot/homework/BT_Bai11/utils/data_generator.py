import time

class DataGenerator:
    @staticmethod
    def random_email(prefix : str):
        timestamp = int(time.time() * 1000)
        return f"{prefix}{timestamp}@chuotbeo.tester.com"