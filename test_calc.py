from Calculator import Calculator
def test_add():
    x,y = 1,2
    instance = Calculator(x,y)
    assert instance.add() == x + y, "Add"

#aca si seria un cambio real?