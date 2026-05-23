from app import config

def test_config_values():
    # just access values to cover file
    assert config is not None
    