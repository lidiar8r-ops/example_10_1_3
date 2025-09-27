import pytest
from src.main_function import calculate_taxes

# 1 задача

@pytest.fixture(scope='module')
def prices():
    return [100, 200, 300]

@pytest.mark.parametrize('tax_rate,  expected_taxes', [(10,[110, 220, 330]),
                                                       (20,[120, 240, 360]),
                                                       (25,[125, 250, 375])])

def test_calculate_taxes(prices, tax_rate,  expected_taxes):
    assert calculate_taxes(prices, tax_rate) ==  expected_taxes


def test_calculate_taxes_value_error(prices):
    with pytest.raises(ValueError):
        calculate_taxes(prices, tax_rate=-1)

def test_calculate_taxes_error_prices(prices):
    with pytest.raises(ValueError):
        calculate_taxes([0, -1], tax_rate=20)


# 2 задача

