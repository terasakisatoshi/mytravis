from mypack import ret_one, twice

def test_twice():
    x = 1
    expected = 2
    assert twice(x) == expected

def test_ret_one():
    expected = 1
    assert ret_one()==expected

