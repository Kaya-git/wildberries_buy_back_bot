# import os
# from dotenv import load_dotenv


# load_dotenv()
# # Database
# DB_USER=os.environ.get("DB_USER")
# DB_HOST=os.environ.get("DB_HOST")
# DB_PASS=os.environ.get("DB_PASS")
# DB_NAME=os.environ.get("DB_NAME")
# DB_PORT=os.environ.get("DB_PORT")

# # Telegram
# BOT_TOKEN = os.environ.get("BOT_TOKEN")
# CHAT_ID = os.environ.get("CHAT_ID")


from dataclasses import dataclass
import os
from dotenv import load_dotenv

from sqlalchemy.engine import URL


load_dotenv()


@dataclass
class DataBaseConfig:
    """ Database connection variables """
    
    name: str = os.environ.get("DB_NAME")
    user: str = os.environ.get("DB_USER")
    passwd: str = os.environ.get("DB_PASS")
    port: str = os.environ.get("DB_PORT")
    host: str = os.environ.get("DB_HOST")
    
    driver: str = "asyncpg"
    database_system: str = "postgresql"
    
    def build_connection_str(self) -> str:
        """ This function build a connection string """
        return URL.create(
            drivername=f"{self.database_system}+{self.driver}",
            username=self.user,
            database=self.name,
            password=self.passwd,
            port=self.port,
            host=self.host,
        ).render_as_string(hide_password=False)


@dataclass
class RedisConfig:
    """ Redis connection variables"""
    
    db: str = int(os.environ.get("REDIS_DATABASE", 1))
    host: str = os.environ.get("REDIS_HOST")
    port: str = os.environ.get("REDIS_PORT")
    # passwd: str = os.environ.get("REDIS_PASSWORD")
    # username: int = os.environ.get("REDIS_USERNAME")
    state_ttl: int = os.environ.get("REDIS_TTL_STATE", None)
    data_ttl: int = os.environ.get("REDIS_TTL_DATA", None)
    

@dataclass
class BotConfig:
    """ Bot Configuration """
    
    token: str = os.environ.get("BOT_TOKEN")


@dataclass
class Configuration:
    """ All in one's configuration class """
    
    debug = bool(os.environ.get("DEBUG"))
    logging_level = int(os.environ.get("LOGGING_LEVEL"))
    
    db = DataBaseConfig()
    redis = RedisConfig()
    bot = BotConfig()

conf = Configuration()
