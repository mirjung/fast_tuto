from typing import Any
from sqlalchemy import inspect

def response_wrapper(status_code: int = None, **kwargs : Any) -> dict:
    return_format = {
        'result': {}
    }
    if status_code:
        return_format['status_code'] = status_code

    for key, value in kwargs.items():
        return_format['result'][key] = value
    return return_format

def obj_as_dict(obj: object) -> dict:
    if obj is not None:
        return {
            c.key: getattr(obj, c.key)
            for c in inspect(obj).mapper.column_attrs
        }
    else:
        return {}