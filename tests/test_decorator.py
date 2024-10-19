from src.decorator import log

def test_log():
    @log
    def wrapper():
        pass