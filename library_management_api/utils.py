from functools import wraps

from drf_yasg.openapi import TYPE_STRING, IN_HEADER,Parameter
from drf_yasg.utils import swagger_auto_schema


def requires_auth(tags, manual_parameters=None):
    if manual_parameters is None:
        manual_parameters = []

    parameters = [
        Parameter(
            "Authorization",
            in_=IN_HEADER,
            type=TYPE_STRING,
            description='Access Token (Include "Bearer " before the token)',
            required=True,
        ),
    ]

    if manual_parameters:
        for item in manual_parameters:
            parameters.append(item)

    def decorator(func):
        @swagger_auto_schema(
            tags=tags,
            responses={200: "OK", 401: "Invalid credentials"},
            manual_parameters=parameters,
        )
        @wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return decorator