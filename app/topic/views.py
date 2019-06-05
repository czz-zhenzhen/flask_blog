# 导入topic蓝图程序用于声明路由
from . import topic


@topic.route('/')
def topic_index():
    return "这是topic中的首页"