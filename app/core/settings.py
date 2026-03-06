from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
	PROJECT_NAME: str = "FastAPI Learning"
	DEBUG_MODE: bool = False
	DATABASE_URL: str = ""
	API_KEY: str = ""
	VERSION: str = "1.0.0"
	model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()