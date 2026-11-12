import pytest

from envios import calc


@pytest.mark.parametrize("weight", [0, 50.001])
def test_def04_invalid_weight_has_exact_message(weight):
    with pytest.raises(ValueError) as error:
        calc(weight, "urbana", "normal", 1)

    assert str(error.value) == "peso inválido"
