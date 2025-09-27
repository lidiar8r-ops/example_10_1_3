import pytest
from src.main_function import calculate_taxes, calculate_tax

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
@pytest.mark.parametrize('price, tax_rate,  expected', [(100, 10, 110),
                                                       (50,5,52.5)])

def test_calculate_tax(price, tax_rate,  expected):
    assert calculate_tax(price, tax_rate) ==  expected


def test_calculate_tax_value_error():
    with pytest.raises(ValueError):
        calculate_tax(-1, 10)


def test_calculate_tax_error_prices_less_0():
    with pytest.raises(ValueError):
        calculate_tax(100, -10)


def test_calculate_tax_error_prices_more_100():
    with pytest.raises(ValueError):
        calculate_tax(100, 1000)
