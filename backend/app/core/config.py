from dotenv import load_dotenv
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

from pydantic_settings import BaseSettings
from pydantic import computed_field
from functools import lru_cache
from typing import List, Literal


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    ALLOWED_ORIGINS: List[str] = []

    ENVIRONMENT: Literal["development", "production", "staging"] = "development"
    API_PREFIX: str = "/api/v1"

    @computed_field
    @property
    def DEBUG(self) -> bool:
        return self.ENVIRONMENT == "development"

    @computed_field
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings() # type: ignore