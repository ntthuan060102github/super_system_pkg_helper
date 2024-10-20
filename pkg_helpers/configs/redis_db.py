from dataclasses import dataclass

@dataclass
class RedisConfig():
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    db: int = ""