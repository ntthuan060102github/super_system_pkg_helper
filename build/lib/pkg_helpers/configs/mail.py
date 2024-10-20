from dataclasses import dataclass

@dataclass
class MailConfig():
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    user_tls: bool = False
    user_ssl: bool = False