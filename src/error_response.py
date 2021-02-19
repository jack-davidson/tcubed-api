class ErrorResponse:
    pass


def err(exception_name: str, message=None):
    response = {"error": exception_name}

    if message:
        response["error_message"] = message

    return response
