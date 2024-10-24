from dataclasses import dataclass

@dataclass
class MailConfig():
    host: str = ""
    port: str = ""
    username: str = ""
    password: str = ""
    use_tls: bool = False
    use_ssl: bool = False