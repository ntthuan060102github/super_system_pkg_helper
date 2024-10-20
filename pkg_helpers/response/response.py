from typing import Union
from rest_framework.response import Response
from pkg_helpers.enums.rest_response_status import RestResponseStatus

class RestResponse():
    content_type = "application/json"

    def __init__(self) -> None:
        self.__data = None
        self.__message = ""
        self.__status = -1
    
    def set_data(self, data: object):
        self.__data = data
        return self
    
    def set_message(self, message: str):
        self.__message = message
        return self
    
    def set_status(self, status: int):
        self.__status = status
        return self
    
    @property
    def response(self):
        return Response(
            {
                "data": self.__data,
                "status": self.__status,
                "message": self.__message,
            },
            content_type=self.content_type
        )
    
    def internal_server_error(self):
        self.__status = RestResponseStatus.INTERNAL_SERVER_ERROR.value[0]
        self.__message = RestResponseStatus.INTERNAL_SERVER_ERROR.value[1]
        return self
    
    def success(self):
        self.__status = RestResponseStatus.SUCCESS.value[0]
        self.__message = RestResponseStatus.SUCCESS.value[1]
        return self
    
    def permission_denied(self):
        self.__status = RestResponseStatus.PERMISSION_DENIED.value[0]
        self.__message = RestResponseStatus.PERMISSION_DENIED.value[1]
        return self
    
    def throttled(self):
        self.__status = RestResponseStatus.THROTTLED.value[0]
        self.__message = RestResponseStatus.THROTTLED.value[1]
        return self
    
    def validation_failed(self):
        self.__status = RestResponseStatus.VALIDATION_FAILED.value[0]
        self.__message = RestResponseStatus.VALIDATION_FAILED.value[1]
        return self
    
    def defined_error(self):
        self.__status = RestResponseStatus.DEFINED_ERROR.value[0]
        self.__message = RestResponseStatus.DEFINED_ERROR.value[1]
        return self
    
    def direct(self, to: str):
        self.__data = {
            "target": to
        }
        self.__status = RestResponseStatus.DIRECT.value[0]
        self.__message = RestResponseStatus.DIRECT.value[1]
        return self
    
    def invalid_token(self):
        self.__status = RestResponseStatus.INVALID_TOKEN.value[0]
        self.__message = RestResponseStatus.INVALID_TOKEN.value[1]
        return self
    
    @property
    def error_type(self) -> Union[RestResponseStatus, None]:
        if self.__status not in RestResponseStatus.value:
            return None
        
        return RestResponseStatus(self.__status)
    
