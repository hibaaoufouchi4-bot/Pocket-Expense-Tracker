from datetime import date
from decimal import Decimal

import pytest

from expense_tracker.records import add_transaction


def test_adds_valid_expense_and_normalizes_category():
    items = []
    result = add_transaction(items, "12.50", "  Food ", "expense", "2026-10-25")
    assert result.amount == Decimal("12.50")
    assert result.category == "Food"
    assert items == [result]


def test_defaults_transaction_date_to_today(monkeypatch):
    class FixedDate(date):
        @classmethod
        def today(cls):
            return cls(2026, 10, 25)
    monkeypatch.setattr("expense_tracker.records.date", FixedDate)
    assert add_transaction([], 2, "Books", "expense").when == FixedDate(2026, 10, 25)


def test_rejects_zero_and_invalid_type():
    with pytest.raises(ValueError):
        add_transaction([], 0, "Food", "expense")
    with pytest.raises(ValueError):
        add_transaction([], 2, "Food", "transfer")
