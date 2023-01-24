import time


class MockDBOperations:
    '''
    Create a class to mimic the database operations.
    This class can be used to implement the actual database operations.
    '''

    # Database initialization
    def __init__(self):
        # A dictionary is used here to store the data
        # Actual database connection can be used to store the data
        self.all_data = {}

    # Add the data to the database

    async def add_data_to_db(self, url: str, short_url: str) -> bool:
        # Sleep is added to simulate the database operation
        time.sleep(0.2)
        try:
            # Check if the url already exists in the database
            if url in self.all_data:
                # If the url already exists, return False
                return False
            else:
                # If the url does not exist, add it to the database
                self.all_data[short_url] = url
                return True
        except:
            return False

    # Delete the data from the database
    async def delete_data_from_db(self, short_url: str) -> bool:
        # Added a sleep to simulate the database operation
        time.sleep(0.2)
        try:
            # Check if the url already exists in the database
            if url in self.all_data:
                # If the url already exists, return False
                return False
            else:
                # If the url does not exist, return False
                return False
        except:
            return False

    # Get the data from the database
    async def fetch_all_data(self) -> dict:
        # added a sleep to simulate the database operation
        time.sleep(0.2)
        # return data
        return self.all_data
