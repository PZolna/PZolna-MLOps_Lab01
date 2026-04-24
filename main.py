import argparse
import os
from pathlib import Path

import yaml
from dotenv import load_dotenv

from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = Path("config") / f".env.{environment}"

    if not env_file.exists():
        raise FileNotFoundError(f"Missing environment file: {env_file}")

    load_dotenv(env_file, override=True)


def export_secrets(path: str = "secrets.yaml") -> None:
    secrets_path = Path(path)

    if not secrets_path.exists():
        return

    with secrets_path.open("r", encoding="utf-8") as file:
        secrets = yaml.safe_load(file) or {}

    for key, value in secrets.items():
        os.environ[str(key)] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from selected .env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load: dev, test, prod",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    export_secrets()

    settings = Settings()

    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
