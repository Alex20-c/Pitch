from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Role, Category, Pitch

# connect to models
from app.models import User

# creating app instance
app = create_app('production')

# create manager instance
manager = Manager(app)

manager.add_command('server', Server)

# create migrate instance
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Category=Category, Pitch=Pitch)


if __name__ == '__main__':
    manager.run()
