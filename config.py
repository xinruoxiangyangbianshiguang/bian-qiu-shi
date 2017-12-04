# coding=utf-8
import redis
class Config(object):
    '''工程配置信息'''
    DEBUG = True
    SECRET_KEY = 'sItmc9bgils3yW6RHE+D4Qfo5SRfLH8jNmzbwOndV/iNHWiN3+pCnABxSOzs9viK'
    # 利用flask_session的扩展，将session数据保存在redis中
    # 创建redis对象，并在配置中填写相关信息
    REDIS_HOST = "127.0.0.1"
    REDIS_POST = 6379

    # 导入数据库扩展，并在配置中填写相关配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/ihome"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # flask_session的配置信息
    SESSION_TYPE = 'redis' # 指定session保存在redis中
    SESSION_USE_SIGNER = True # 让cookie中的session_id 做加密处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_POST)
    PERMANENT_SESSION_LIFETIME = 86400 # session 的有效期 单位为秒

	
	shiren 