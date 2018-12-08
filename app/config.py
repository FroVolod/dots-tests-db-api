from pathlib import Path


class Configuration(object):
    DEBUG = True
    TESTS_FOLDER = Path('./test_db').resolve()