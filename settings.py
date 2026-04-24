from pydantic import field_validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ENVIRONMENT: str
    APP_NAME: str
    API_KEY: str | None = None

    @field_validator("ENVIRONMENT")
    @classmethod
    def validate_environment(cls, value: str) -> str:
        allowed_environments = {"dev", "test", "prod"}

        if value not in allowed_environments:
            raise ValueError("ENVIRONMENT must be one of: dev, test, prod")

        return value
