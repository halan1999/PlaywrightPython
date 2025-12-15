import time

class DataGenerator:
    def create_input_data_name(prefix : str):
        timestamp = int(time.time() * 1000)
        return f"{prefix}_{timestamp}"