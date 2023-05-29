from typing import Any
from pydantic import BaseSettings, Field, validator


class Settings(BaseSettings):
    BASE_KEYS: list[str] = Field(
        env='BASE_KEYS',
        default=[
            '397Npr2h-e86Rw0H4-a38nzO62'
        ]
    )
    THREADS_COUNT: int = Field(env='THREADS_COUNT', default=1)
    PROXY_FILE: str | None = Field(env='PROXY_FILE', default=None)
    DEVICE_MODELS: list[str] = Field(env='DEVICE_MODELS', default=[])
    DELAY: int = Field(env='DELAY', default=25)
    OUTPUT_FILE: str = Field(env='OUTPUT_FILE', default='output.txt')
    OUTPUT_FORMAT: str = Field(env='OUTPUT_FORMAT', default='{key} | {referral_count}')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

        @classmethod
        def parse_env_var(cls, field: str, raw_val: str) -> Any:
            if field == 'BASE_KEYS' or field == 'DEVICE_MODELS':
                if isinstance(raw_val, str):
                    return str(raw_val).split(',')

            return cls.json_loads(raw_val) # type: ignore

config = Settings()
