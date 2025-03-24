from flask import Flask, jsonify
from extension import db, cors
from sqlalchemy import text
from models import Drug, DiseaseEFO, DiseaseOMIM, Literature
from flask.views import MethodView
from routes import all_blueprints


app = Flask(__name__)

# 数据库配置
HOSTNAME = "127.0.0.1"
PORT = 3306
USERNAME = "root"
PASSWORD = "1234"
DATABASE = "drugweb"
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8mb4"


# 初始化 db（要在设置 config 后）
db.init_app(app)
cors.init_app(app)

# 测试数据库连接
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))  # ✅ 改为 text()
        print(rs.fetchone())

# 注册所有蓝图
for bp in all_blueprints:
    app.register_blueprint(bp)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
