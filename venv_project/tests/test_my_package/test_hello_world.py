from src.my_package.hello_world import my_hello_world


def test_hello_world():
    assert my_hello_world() == "Hello world: 3!"
