# coding=utf-8


# 站点相关配置
config = dict(
    debug=False,
    log_level="WARNING",
    log_file=True,
    log_console=False,
    log_file_path="logs/log",
    login_url="/login",
    port=8989,
    # base64.b64encode(str(uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid4()))))
    cookie_secret='YmNmNmQzNmMtOWI5MS01YTJiLWEzYWItMGI2ZmFkOTkzY2Ji',
    xsrf_cookies=True,


)