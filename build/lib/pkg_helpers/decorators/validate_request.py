from functools import wraps
from pkg_helpers.response.response import RestResponse
from pkg_helpers.logging import logger

def validate_request(validate_class):
    def callback_handler(callback):
        @wraps(callback)
        def wrapper(self, request, **kwargs):
            try:
                validate = validate_class(data=request.data)

                if not validate.is_valid():
                    return RestResponse().validation_failed().set_data(validate.errors).response
            except Exception as e:
                logger.exception("pkg_helpers.decorators.validate_request exc=%s", e)
                return RestResponse().internal_server_error().response
            return callback(self, request, validate.validated_data, **kwargs)
        return wrapper
    return callback_handler