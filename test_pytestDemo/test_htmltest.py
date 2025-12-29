import pytest


@pytest.mark.green
def test_base_fixture():
    print("I am the main and i should execute first")