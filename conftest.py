import pytest
from flask import Flask

@pytest.fixture(scope='module')
def app() -> Flask:
    from app import Handler
    handler = Handler()
    handler.app.register_error_handler(Exception, handler.app_error)
    handler.app.add_url_rule('/shortanswer', 'shortanswer', handler.make_short_answer, methods=['post'])
     
    return handler.app
