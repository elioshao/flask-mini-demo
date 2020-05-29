from flask import Response
from functools import wraps
from flask import request

from flasgger import Swagger


class SwaggerExtensions:
    @classmethod
    def requires_basic_auth(cls, user_name, pass_word):
        def inner(f):
            """Decorator to require HTTP Basic Auth for your endpoint."""

            def check_auth(username, password):
                return username == user_name and password == pass_word

            def authenticate():
                return Response(
                    "Authentication required.",
                    401,
                    {"WWW-Authenticate": "Basic realm='Login Required'"},
                )

            @wraps(f)
            def decorated(*args, **kwargs):
                # NOTE: This example will require Basic Auth only when you run the
                # app directly. For unit tests, we can't block it from getting the
                # Swagger specs so we just allow it to go thru without auth.
                # The following two lines of code wouldn't be needed in a normal
                # production environment.
                auth = request.authorization
                if not auth or not check_auth(auth.username, auth.password):
                    return authenticate()
                return f(*args, **kwargs)

            return decorated

        return inner

    @classmethod
    def init_app(cls, app):
        app.config["SWAGGER"] = {"title": app.config.get("TITLE"), "uiversion": 3}
        Swagger.DEFAULT_CONFIG["specs_route"] = app.config.get("API_URL")
        Swagger(
            app,
            decorators=[
                cls.requires_basic_auth(
                    app.config.get("USERNAME"), app.config.get("PASSWORD")
                )
            ],
            template={
                "swagger": "2.0",
                "info": {"title": app.config.get("SUB_TITLE"), "version": "1.0"},
                "consumes": ["application/json"],
                "produces": ["application/json"],
            },
        )
