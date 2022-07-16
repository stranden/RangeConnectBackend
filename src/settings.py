import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_connection_uri: str