import pytest
from data import Data
from user import User
from products import Products
from main import load_products, simulate_user_views, get_recommendations

@pytest.fixture
def data_with_products():
    data = Data()
    load_products(data, Products.products)
    return data

@pytest.fixture
def test_user():
    return User(
        "product_003", "product_005", "product_008", "product_012",
        "product_017", "product_021", "product_025", "product_028",
        "product_034", "product_037", "product_042", "product_050"
     )

def test_load_products(data_with_products):
    all_products = data_with_products.get_sorted_by_score()
    assert len(all_products) > 0
    for p in all_products:
        assert "category" in p
        assert "subcategory" in p

def test_simulate_user_views(data_with_products, test_user):
    simulate_user_views(data_with_products, test_user)
    for k in test_user.seen:
        prod = data_with_products.get_product(k)
        assert prod is not None
        assert prod["score"] == 1

def test_get_recommendations(data_with_products, test_user):
    simulate_user_views(data_with_products, test_user)
    recs = get_recommendations(data_with_products, test_user)
    assert isinstance(recs, list)
    for r in recs:
        assert r["key"] not in test_user.seen
        assert "category" in r
        assert "subcategory" in r
