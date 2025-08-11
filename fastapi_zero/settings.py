from pydantic_settings import BaseSettings, SettingsConfigDict


# TODO Continue https://www.youtube.com/watch?v=I7IrmN7jMqE 1:25:00
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    DATABASE_URL: str
    DATABASE_URL: str
