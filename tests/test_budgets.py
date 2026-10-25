from datetime import date
from decimal import Decimal

import pytest

from expense_tracker.budgets import budget_status
from expense_tracker.records import add_transaction


def test_budget_counts_only_matching_category_month_expenses():
    items = []
    add_transaction(items, 30, "Food", "expense", "2026-10-03")
    add_transaction(items, 10, "food", "expense", "2026-10-20")
    add_transaction(items, 90, "Food", "expense", "2026-09-20")
    add_transaction(items, 50, "Food", "income", "2026-10-20")
    result = budget_status(items, "FOOD", 50, 2026, 10)
    assert result["spent"] == Decimal("40")
    assert result["remaining"] == Decimal("10")
    assert result["within_budget"] is True


def test_budget_limit_is_inclusive_at_boundary():
    items = []
    add_transaction(items, 50, "Travel", "expense", date(2026, 10, 1))
    assert budget_status(items, "Travel", 50, 2026, 10)["within_budget"] is True


def test_rejects_invalid_month_and_nonpositive_limit():
    with pytest.raises(ValueError):
        budget_status([], "Food", 10, 2026, 13)
    with pytest.raises(ValueError):
        budget_status([], "Food", 0, 2026, 10)
