# Launch the script
import os
from app import create_app
from flask_script import Manager, Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

@manager.command
def deploy():
    """Run deployment tasks."""
    pass

if __name__ == '__main__':
    manager.run()