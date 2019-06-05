# 主要工作创建Flask应用实例以及各种配置
# 创建SQLALcjemy的应用实例
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
pymysql.install_as_MySQLdb()
db = SQLAlchemy()
def create_app():
    # 创建Flask程序实例
    app = Flask(__name__)
    app.config['DEBUG']=True
    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:123456@localhost:3306/blog_new"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'czz'
   # 关联app与创建好的db实例
    db.init_app(app)
    # 讲topic蓝图新恒旭与app关联到一起
    from .topic import topic as topic_blueprint
    app.register_blueprint(topic_blueprint)
    # 创建好的程序实例返回
    return app
