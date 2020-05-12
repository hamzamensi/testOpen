from exercice1 import serialize, deserialize


def test_serialize():
    assert serialize([]) == ""
    assert serialize(['Ceci', 'est', 'un', 'test']) == 'Ceci est un test'


def test_serialize():
    assert deserialize('') == []
    assert deserialize('Ceci est un test') == ['Ceci', 'est', 'un', 'test']
