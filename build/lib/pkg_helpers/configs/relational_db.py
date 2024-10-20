from dataclasses import dataclass

@dataclass
class RelationalDatabaseConfig():
    engine: str = ""
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    db_name: str = ""