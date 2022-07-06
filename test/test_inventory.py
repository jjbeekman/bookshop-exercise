from inventory import calculate_inventory, calculate_best_sellers
import pytest


TRANSACTION_LOG = """17000372214424 INCOMING 9
17000372214424 OUTGOING 1
17000372214424 INCOMING 3
42100551007975 OUTGOING 3
42100551007975 INCOMING 1
17000372214424 OUTGOING 4
25234531007903 OUTGOING 4
25234531007903 INCOMING 7"""


class TestCalculateInventory:
    def test_calculate_inventory(self):
        """CIN 17000372214424 increases by 7 and CIN 42100551007975 drops by 2"""
        start_inventory = {
            "17000372214424": 4,
            "42100551007975": 9,
            "25234531007903": 3,
        }

        inventory = calculate_inventory(start_inventory=start_inventory, transaction_log=TRANSACTION_LOG)

        assert inventory == {
            "17000372214424": 11,
            "42100551007975": 7,
            "25234531007903": 6,
        }

    def test_calculate_inventory_faulty_transaction_log(self):
        """CIN 42100551007977 is invalid"""
        start_inventory = {}
        transaction_log = "42100551007977 INCOMING 1"

        with pytest.raises(AssertionError):
            calculate_inventory(start_inventory=start_inventory, transaction_log=transaction_log)

    def test_calculate_inventory_missing_cin(self):
        """CIN 17000372214424 is not defined in the start inventory"""
        start_inventory = {
            "42100551007975": 9,
            "25234531007903": 6,
        }

        inventory = calculate_inventory(start_inventory=start_inventory, transaction_log=TRANSACTION_LOG)

        assert inventory == {
            "17000372214424": 7,
            "42100551007975": 7,
            "25234531007903": 9,
        }

    def test_calculate_inventory_negative_value(self):
        """CIN 42100551007975 will drop to -2 in the final inventory"""
        start_inventory = {}

        with pytest.raises(ValueError):
            calculate_inventory(start_inventory=start_inventory, transaction_log=TRANSACTION_LOG)


class TestCalculateBestSellers:
    def test_calculate_best_sellers(self):
        """CIN 42100551007975 should not show because it has negative sells"""
        result = calculate_best_sellers(transaction_log=TRANSACTION_LOG, n=3)
        assert len(result) == 2
        assert result[0].cin == "17000372214424"
        assert result[1].cin == "25234531007903"

    def test_calculate_best_sellers_publication_type(self):
        """Only CIN 25234531007903 should be shown because this is the desired publication type"""
        result = calculate_best_sellers(transaction_log=TRANSACTION_LOG, n=3, publication_type="25")
        assert len(result) == 1
        assert result[0].cin == "25234531007903"

    def test_calculate_best_sellers_n(self):
        """Test the n-parameter by only showing the top-1 BestSeller"""
        result = calculate_best_sellers(transaction_log=TRANSACTION_LOG, n=1)
        assert len(result) == 1
        assert result[0].cin == "17000372214424"
