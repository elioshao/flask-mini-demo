from flask_jwt_extended import JWTManager, get_jwt_claims


class UserJwt:
    """重新封装的User对象，给jwt的current_user使用"""

    def __init__(self, id, username, admin):
        self.id = id
        self.username = username
        self.admin = admin


class JwtExtensions:
    @classmethod
    def init_app(cls, app):
        jwt = JWTManager(app)

        @jwt.user_claims_loader
        def user_to_claims(user):
            return UserJwt(user.id, user.username, user.admin).__dict__

        @jwt.user_loader_callback_loader
        def user_loader_callback(identity):
            user = get_jwt_claims()
            return UserJwt(user["id"], user["username"], user["admin"])

        @jwt.user_identity_loader
        def user_identity_lookup(user):
            return user.username
