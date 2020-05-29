import os
from flask import Flask

from BasicDemo.extentions.cache import cache
from BasicDemo.extentions.limiter import limiter
from BasicDemo.extentions.db import db
from BasicDemo.extentions.redis import redis
from BasicDemo.extentions.swagger import SwaggerExtensions
from BasicDemo.extentions.jwt import JwtExtensions
from BasicDemo.extentions.log import LogExtensions


def create_app(config=None, instance_path=None):
    app = Flask("BasicDemo", instance_path=instance_path, instance_relative_config=True)
    # instance folders are not automatically created by flask
    if not os.path.exists(app.instance_path):
        os.makedirs(app.instance_path)
    configure_app(app, config)
    configure_blueprints(app)
    configure_extensions(app)
    configure_request_handlers(app)
    return app


def configure_app(app, config):
    """配置app"""
    app.config.from_object("BasicDemo.configs.default.DefaultConfig")


def configure_blueprints(app):
    """配置蓝图"""
    from BasicDemo.views.admin.home import load_admin_home_blueprints
    from BasicDemo.views.auth.login import load_auth_blueprints

    load_admin_home_blueprints(app)
    load_auth_blueprints(app)


def configure_extensions(app):
    """配置扩展组件"""
    cache.init_app(app)
    limiter.init_app(app)
    db.init_app(app)
    redis.init_app(app)
    SwaggerExtensions.init_app(app)
    JwtExtensions.init_app(app)
    LogExtensions.init_app(app)


def configure_request_handlers(app):
    """配置"""

    @app.after_request
    def after_request(response):
        db.session.close()
        return response

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()
