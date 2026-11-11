class api_fetcher:
    def fetch_data(self):
        return "Fetching data from API"

class database_fetcher:
    def fetch_data(self):
        return "Fetching data from Database"
    
class s3_fetcher:
    def fetch_data(self):
        return "Fetching data from S3"

obj = api_fetcher()
print(obj.fetch_data())