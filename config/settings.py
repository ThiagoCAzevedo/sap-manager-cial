from pydantic_settings import BaseSettings
from pydantic import Field


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

    class Config:
        env_file = "config/.env"
        extra = "forbid"
        case_sensitive = True


settings = Settings()