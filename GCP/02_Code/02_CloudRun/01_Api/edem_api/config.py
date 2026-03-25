from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_ID: str

settings = Settings()