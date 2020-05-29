class ErrorCodeMsg(Exception):
    def __init__(self, value=None, code=20000, message="unexpected error"):
        if isinstance(value, dict):
            self.code = value.get("code", code)
            self.message = value.get("message", message)
        elif isinstance(value, tuple):
            self.code = value[1]
            self.message = value[0]
        elif isinstance(value, str):
            self.code = code
            self.message = value
        else:
            self.code = code
            self.message = message
        super().__init__(self.message)

    @property
    def response(self) -> dict:
        return {"message": self.message, "error_code": self.code}

    @property
    def code_msg(self) -> tuple:
        return self.message, self.code


class ErrorCodeMsgSet:
    """
    定义全部的ErrorCode

    code: 20502
    2	                    05	        02
    服务级错误（1为系统级错误）	服务模块代码	具体错误代码
    """

    # 系统错误
    UNEXPECTED_ERROR = ErrorCodeMsg({"code": 20000, "message": "unexpected error"})
    # 参数错误 **不要使用** wtf验证默认error code, message不具体定义(前端定义显示message)
    PARAMETER_ERROR = ErrorCodeMsg({"code": 20001, "message": "parameter error"})

    # 通用error code
    # ------------------------------------------------------------------------------------
    # 非法内容
    ILLEGAL_CONTENT = ErrorCodeMsg({"code": 20002, "message": "illegal content"})
    # 密码错误
    PASSWORD_ERROR = ErrorCodeMsg({"code": 20003, "message": "password error"})
    # 手机号错误
    MOBILE_ERROR = ErrorCodeMsg({"code": 20004, "message": "mobile error"})
    # 手机号已存在
    MOBILE_EXIST = ErrorCodeMsg({"code": 20005, "message": "mobile exist"})
    # 手机号未注册
    MOBILE_NOT_REGISTER = ErrorCodeMsg(
        {"code": 20006, "message": "mobile not register"}
    )
    # 用户已存在
    USER_EXIST = ErrorCodeMsg({"code": 20007, "message": "user exist"})
    # 用户不存在
    USER_NOT_EXIST = ErrorCodeMsg({"code": 20008, "message": "user not exist"})
    # 子账号已存在
    SUBACCOUNT_EXIST = ErrorCodeMsg({"code": 20009, "message": "subaccount exist"})
    # 子账号不存在
    SUBACCOUNT_NOT_EXIST = ErrorCodeMsg(
        {"code": 20010, "message": "subaccount not exist"}
    )
    # 子账号数超出限制
    SUBACCOUNT_EXCEEDS_LIMIT = ErrorCodeMsg(
        {"code": 20011, "message": "subaccount exceeds limit"}
    )
    # 币种不存在
    CURRENCY_NOT_EXIST = ErrorCodeMsg({"code": 20012, "message": "currency not exist"})
    # 验证码错误
    IDENTIFY_CODE_ERROR = ErrorCodeMsg(
        {"code": 20013, "message": "identify code error"}
    )

