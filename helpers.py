from typing import List, Tuple
from cin import is_valid_cin


def interpret_transaction_log(transaction_log: str) -> List[Tuple[str, int]]:
    """
    The transaction log is supplied as a string that should be interpreted.

    This function should raise a readable exception for any faulty formatting
    """
    transactions = []

    for line in transaction_log.split("\n"):
        cin, action, value = line.split(" ")
        value = int(value)
        assert is_valid_cin(cin), f"CIN [{cin}] is invalid"
        assert value > 0, "Values must be positive"

        if action == "INCOMING":
            transactions.append((cin, value))
        elif action == "OUTGOING":
            transactions.append((cin, -value))
        else:
            raise AssertionError("Action should be INCOMING or OUTGOING")

    return transactions
