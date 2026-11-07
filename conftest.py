import pytest

def pytest_configure(config):
    config.addinivalue_line("markers", "hardware: requires physical hardware")
