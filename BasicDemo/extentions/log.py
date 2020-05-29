import logging


class LogExtensions:
    @classmethod
    def init_app(cls, app):
        app.logger.setLevel(logging.INFO)
