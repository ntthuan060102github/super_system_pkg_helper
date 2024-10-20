import json
import inspect
from typing import Any

from pkg_helpers.logging import logger
from pkg_helpers.configs.mail import MailConfig
from pkg_helpers.configs.redis_db import RedisConfig
from pkg_helpers.configs.relational_db import RelationalDatabaseConfig

class BaseConfig():
    relational_database: RelationalDatabaseConfig = None
    redis_database: RedisConfig = None
    remote_log_token: str = ""
    mail: MailConfig = None

    def __init__(self) -> None:
        self.__load_config_from_config_file()

    def __load_config_from_config_file(self):
        try:
            with open('config.json') as file:
                config = json.load(file)
                logger.exception("BaseConfig.__load_config_from_config_file config=%s", config)

                for attr in inspect.getmembers(self):
                    if not attr[0].startswith('_'):
                        if not inspect.ismethod(attr[1]): 
                            if attr[0] in config:
                                if self.__is_primitive(config[attr[0]]):
                                    setattr(self, attr[0], config[attr[0]])

                                elif isinstance(config[attr[0]], dict):
                                    setattr(self, attr[0], self.__annotations__.get(attr[0])(**config[attr[0]]))
        except Exception as e:
            logger.exception("BaseConfig.__load_config_from_config_file exc=%s", e)

    def __is_primitive(self, obj: Any) -> bool:
        primitives = (bool, str, int, float, type(None))
        return isinstance(obj, primitives)

