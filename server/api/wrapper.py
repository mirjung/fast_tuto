from fastapi import status
def response_wrapper(status_code: status = None, **kwargs) -> dict:
    return_format = {
        'result': {}
    }
    if status_code:
        return_format['status_code'] = status_code

    for key, value in kwargs.items():
        return_format['result'][key] = value
    return return_format