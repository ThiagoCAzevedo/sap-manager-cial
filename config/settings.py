from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field
import os


class Settings(BaseSettings):
    # APP CONFIG
    APP_NAME: str
    APP_URL: str
    FILES_DRIVER: str

    # SAP LOGIN
    SAP_PATH: str
    SAP_CONNECTION_NAME: str
    SAP_USER: str
    SAP_PSWD: str

    model_config = SettingsConfigDict(
        env_file="config/.env.test" if os.getenv("TESTING") == "true" else "config/.env",
        extra="forbid",
        case_sensitive=True,
    )


settings = Settings()