from pydantic_settings import BaseSettings

from .environment import Environment
from .settings import Settings

ENV_FILENAMES = {
    Environment.DEV: (".env.dev",),
    Environment.PROD: (".env.prod",),
    Environment.TEST: (".env.test",),
}


class EnvironmentSettingsLoader(BaseSettings):
    """Configuration class responsible for loading application settings based on the environment.

    It determines the appropriate environment file (`.env.prod`, `.env.dev`, or `.env.test`)
    and uses it to populate a `Settings` instance.
    """

    ENVIRONMENT: Environment = Environment.DEV

    def load_settings(self) -> Settings:
        """Creates an instance of `Settings` based on the current environment.

        Returns:
            Settings: The instance of `Settings` loaded from the environment-specific file.
        """
        env_filename = ENV_FILENAMES[self.ENVIRONMENT]
        return Settings(_env_file=env_filename)


settings: Settings = EnvironmentSettingsLoader().load_settings()

__all__ = ["settings"]
