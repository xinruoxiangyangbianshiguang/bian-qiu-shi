# coding=utf-8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager
from config import Config
app = Flask(__name__)

# 先在当前类中定义配置的类，并从中加载配置



app.config.from_object(Config)
#CSRFProtect只做验证工作，cookie中的csrf_token和表单提交里的csrf_token 需要我们自己实现
csrf = CSRFProtect(app)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_POST)
manager = Manager(app)
Migrate(app, db)
manager.add_command('db',MigrateCommand)

@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run(debug=True)