from flask.views import MethodView

from BasicDemo.libs.utils import RegisterView
from BasicDemo.auth.decorators import admin_required
from BasicDemo.views.admin import admin


class HomeView(MethodView):
    decorators = (admin_required,)

    def get(self):
        """
        banner设置
        ---
        tags:
           - 后台管理接口
        parameters:
            -   name: pk
                in: query
                required: false
                description: id
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
        return "hello world"


def load_admin_home_blueprints(app):
    RegisterView.register_view(
        admin, routes=["/home/"], view_func=HomeView.as_view("home")
    )
    app.register_blueprint(admin, url_prefix=app.config["ADMIN_HOME_URL_PREFIX"])
