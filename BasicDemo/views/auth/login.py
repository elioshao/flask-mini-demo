from flask.views import MethodView
from flask import current_app
from flask_jwt_extended import (
    set_access_cookies,
    set_refresh_cookies,
    create_access_token,
    create_refresh_token,
)

from BasicDemo.libs.utils import RegisterView
from BasicDemo.views.auth import auth


class LoginView(MethodView):

    def post(self):
        """
        登录
        ---
        tags:
           - 认证接口
        parameters:
            -   name: username
                in: body
                required: true
                description: 用户名
            -   name: password
                in: body
                required: true
                description: 密码
        responses:
            200:
                examples:
                    返回数据: [
                                {
                                    "priority": 1,
                                    "color": "1",
                                    "content": "啦啦啦",
                                    "image": "http://www.qq.com/qq.png",
                                    "url": "http://www.qq.com",
                                },....
                            ]
            测试链接:
                description: http://127.0.0.1:3000/v1/admin/home
        """
        from BasicDemo.extentions.jwt import UserJwt

        user = UserJwt(1, "admin", 1)
        resp = current_app.make_response(
            {"message": "login succeed", "role": user.admin, "id": user.id}
        )
        set_access_cookies(resp, create_access_token(identity=user))
        set_refresh_cookies(resp, create_refresh_token(identity=user))
        return resp


def load_auth_blueprints(app):
    RegisterView.register_view(
        auth, routes=["/login/"], view_func=LoginView.as_view("login")
    )
    app.register_blueprint(auth, url_prefix=app.config["AUTH_HOME_URL_PREFIX"])
