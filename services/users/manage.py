#!/usr/bin/env python3
# users/manage.py
import sys
import unittest
import coverage

from flask.cli import FlaskGroup

from app import create_app, db

COV = coverage.coverage()
COV.start()

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command()
def test():
    test = unittest.TestLoader().discover('app/test/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(test)

    if result.wasSuccessful():
        return 0

    sys.exit(result)

@cli.command()
def cov():
    test = unittest.TestLoader().discover('app/test/', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(test)

    if result.wasSuccessful():
        COV.stop()
        COV.save()
        print("Coverage summary: ")
        COV.report()
        COV.html_report()
        COV.erase()
        return 0
    
    sys.exit(result)

if __name__ == '__main__':
    cli()


