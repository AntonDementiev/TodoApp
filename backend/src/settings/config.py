import os
from dotenv import load_dotenv
from envparse import Env
from abc import ABC, abstractmethod


class DatabaseConfig(ABC):
    @abstractmethod
    def get_database_url(self) -> str:
        pass


class EnvDatabaseConfig(DatabaseConfig):
    def __init__(self):
        load_dotenv()
        self.env = Env()

    def get_database_url(self) -> str:
        db_host = os.getenv("DB_HOST")
        db_port = os.getenv("DB_PORT")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        db_pass = os.getenv("DB_PASS")
        
        return self.env.str(
            "DATABASE_URL", 
            default=f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
        )

class DatabaseManager:
    def __init__(self, config: DatabaseConfig):
        self._config = config

    def get_connection_url(self) -> str:
        return self._config.get_database_url()

config = EnvDatabaseConfig()
db_manager = DatabaseManager(config)
DATABASE_URL = db_manager.get_connection_url()
