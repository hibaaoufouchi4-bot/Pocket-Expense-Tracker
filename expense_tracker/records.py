"""Transaction creation and input validation (Feature A)."""

from dataclasses import dataclass
from datetime import date
from decimal import Decimal, InvalidOperation


@dataclass(frozen=True)
class Transaction:
    amount: Decimal
    category: str
    kind: str
    when: date
    note: str = ""


def add_transaction(transactions, amount, category, kind, when=None, note=""):
    """Validate and append a transaction; amounts are positive magnitudes."""
    try:
        value = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("amount must be a valid number") from None
    if not value.is_finite() or value <= 0:
        raise ValueError("amount must be greater than zero")

    clean_category = str(category).strip()
    if not clean_category:
        raise ValueError("category cannot be empty")
    if kind not in {"income", "expense"}:
        raise ValueError("kind must be 'income' or 'expense'")

    if when is None:
        when = date.today()
    elif isinstance(when, str):
        try:
            when = date.fromisoformat(when)
        except ValueError:
            raise ValueError("date must use YYYY-MM-DD format") from None
    if not isinstance(when, date):
        raise ValueError("when must be a date or YYYY-MM-DD string")

    transaction = Transaction(value, clean_category, kind, when, str(note).strip())
    transactions.append(transaction)
    return transaction
