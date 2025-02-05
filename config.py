from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_PASSWORD: str
    DB_USERNAME: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str

    model_config = SettingsConfigDict(env_file='.env')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.DB_URL = f"postgresql+asyncpg://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


config = Settings()
