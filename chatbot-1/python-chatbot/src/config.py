import os

class Config:
    @staticmethod
    def load_env():
        from dotenv import load_dotenv
        load_dotenv()

    @staticmethod
    def get_database_url():
        return os.getenv("DATABASE_URL")

    @staticmethod
    def get_api_key():
        return os.getenv("API_KEY")