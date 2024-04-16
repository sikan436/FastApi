from pydantic.v1 import BaseSettings

class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_username: str
    database_name: str
    secret_key: str
    algorithm: str
    access_token_expire_min: int

    class Config:
        env_file = ".env"
        extra="allow"


settings=Settings()
