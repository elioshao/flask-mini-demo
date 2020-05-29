# -*- coding: utf-8 -*-
"""
    flaskbb.configs.default
    ~~~~~~~~~~~~~~~~~~~~~~~

    This is the default configuration for FlaskBB that every site should have.
    You can override these configuration variables in another class.

    :copyright: (c) 2014 by the FlaskBB Team.
    :license: BSD, see LICENSE for more details.
"""
import os
import sys
import datetime


class DefaultConfig(object):
    # 获取项目目录
    basedir = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    )
    # python的版本
    py_version = "{0.major}{0.minor}".format(sys.version_info)
    # flask的配置信息
    DEBUG = False
    TESTING = "develop"
    SECRET_KEY = "default"
    # swagger配置
    API_URL = "/v1/apidocs/"
    USERNAME = "admin"
    PASSWORD = "admin"
    TITLE = "最小应用接口文档"
    SUB_TITLE = "最小应用接口文档"
    # 数据库配置
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + "/" + "flaskbb.sqlite"
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_BINDS = {}
    # jwt config
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_COOKIE_SECURE = False
    JWT_COOKIE_DOMAIN = "test.***.com"
    JWT_CSRF_IN_COOKIES = True
    JWT_ACCESS_COOKIE_PATH = "/"
    JWT_ACCESS_CSRF_COOKIE_PATH = "/"
    JWT_REFRESH_COOKIE_PATH = "/"
    JWT_REFRESH_CSRF_COOKIE_PATH = "/"
    JWT_COOKIE_CSRF_PROTECT = True
    JWT_CSRF_METHODS = ["GET", "PUT", "POST", "DELETE"]
    JWT_ERROR_MESSAGE_KEY = "message"
    JWT_CLAIMS_IN_REFRESH_TOKEN = True
    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=7)
    JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=30)
    JWT_SESSION_COOKIE = False
    JWT_SECRET_KEY = "default"
    # 缓存设置
    CACHE_TYPE = "redis"
    CACHE_DEFAULT_TIMEOUT = 60
    CACHE_KEY_PREFIX = "default_cache"
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    # 频率限制设置
    RATELIMIT_STORAGE_URL = "redis://localhost:6379/1"
    RATELIMIT_KEY_PREFIX = "default_limit"
    RATELIMIT_HEADERS_ENABLED = True
    RATELIMIT_SWALLOW_ERRORS = True
    RATELIMIT_IN_MEMORY_FALLBACK = True
    # URL Prefixes
    USER_HOME_URL_PREFIX = "/user"
    ADMIN_HOME_URL_PREFIX = "/admin"
    AUTH_HOME_URL_PREFIX = "/auth"

    DEFAULT_RENDERERS = ["flask_api.renderers.JSONRenderer"]
