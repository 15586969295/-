from back_end import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# 创建app
app = create_app()
# 集成flask-script
manager = Manager(app)
# 将 app 与 db 关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return "index"


if __name__ == '__main__':
    manager.run()
