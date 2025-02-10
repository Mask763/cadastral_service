from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_PASSWORD: str
    DB_USERNAME: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: str
    JWT_SECRET: str

    model_config = SettingsConfigDict(env_file='../.env')

    @property
    def DB_URL(self) -> str:
        return (f"postgresql+asyncpg://{self.DB_USERNAME}:"
                f"{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/"
                f"{self.DB_NAME}")


config = Settings()
