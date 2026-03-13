from app import add

def test_add_correct():
    # This should pass
    assert add(2, 3) == 5

def test_add_wrong():
    # This will FAIL to show you how the pipeline reacts
    assert add(2, 2) == 5 
