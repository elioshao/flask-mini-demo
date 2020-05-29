class RegisterView:
    @classmethod
    def register_view(cls, bp_or_app, routes, view_func, *args, **kwargs):
        """动态添加试图函数"""
        for route in routes:
            bp_or_app.add_url_rule(route, view_func=view_func, *args, **kwargs)
