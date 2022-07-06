from collections.abc import Mapping
from collections import defaultdict
from typing import Optional
from helpers import interpret_transaction_log
from best_sellers import BestSeller


def calculate_inventory(start_inventory: Mapping[str, int], transaction_log: str) -> dict[str, int]:
    """
    Calculate the new inventory stock based on the transaction log of the day
    """
    inventory = defaultdict(int)
    for cin, value in start_inventory.items():
        inventory[cin] = value

    inventory = __process_transaction_log(inventory=inventory, transaction_log=transaction_log)
    __assert_stock_is_positive(inventory)

    return dict(inventory)


def calculate_best_sellers(transaction_log: str, n: int, publication_type: Optional[str] = None) -> list[BestSeller]:
    """
    Interpret the transaction log and determine the best sellers based on this.
    The return values can be filtered by amount of best sellers and/or publication type
    """
    sales = __process_transaction_log(inventory=defaultdict(int), transaction_log=transaction_log)
    ordered_sales = sorted(sales.items(), key=lambda x: (-x[1], x[0]))
    if publication_type:
        assert isinstance(publication_type, str), "Define the publication type as a string"
        assert len(publication_type) == 2, "Publication type should be the first two digits of the CIN"
        ordered_sales = [(cin, sold) for cin, sold in ordered_sales if cin[:2] == publication_type]
        print(ordered_sales)

    best_sellers = [
        BestSeller(cin=cin, publication_type=cin[:2], quantity_sold=sold) for cin, sold in ordered_sales[:n] if sold > 0
    ]
    return best_sellers


def __process_transaction_log(inventory: Mapping[str, int], transaction_log: str) -> Mapping[str, int]:
    """
    Processes the transaction log file and updates the inventory mapping
    """
    transactions = interpret_transaction_log(transaction_log)
    for cin, value in transactions:
        inventory[cin] += value

    return inventory


def __assert_stock_is_positive(inventory: Mapping[str, int]):
    """
    Raises a ValueError indicating all CINs that have dropped below 0 at the end of the day
    """
    negative_cin = [cin for cin, stock in inventory.items() if stock < 0]
    if negative_cin:
        raise ValueError(f"Encountered a negative stock value for following CINs: {negative_cin}")
