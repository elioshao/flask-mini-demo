from flask_api import status


class ApiError:
    @staticmethod
    def unauthorized(message, error_code=None):
        return ApiError.error(status.HTTP_401_UNAUTHORIZED, message, error_code)

    @staticmethod
    def bad_request(message, error_code=None):
        return ApiError.error(status.HTTP_400_BAD_REQUEST, message, error_code)

    @staticmethod
    def not_found(message, error_code=None):
        return ApiError.error(status.HTTP_404_NOT_FOUND, message, error_code)

    @staticmethod
    def forbidden(message, error_code=None):
        return ApiError.error(status.HTTP_403_FORBIDDEN, message, error_code)

    @staticmethod
    def internal_error(message):
        return ApiError.error(status.HTTP_500_INTERNAL_SERVER_ERROR, message, None)

    @staticmethod
    def error(http_code, message, error_code=None):
        if error_code:
            return {"message": message, "error_code": error_code}, http_code
        return {"message": message}, http_code
