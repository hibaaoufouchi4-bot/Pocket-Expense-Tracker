from decimal import Decimal

import pytest

from expense_tracker.records import add_transaction
from expense_tracker.summaries import monthly_summary


def test_monthly_summary_totals_and_category_breakdown():
    items = []
    add_transaction(items, 1000, "Salary", "income", "2026-10-01")
    add_transaction(items, 40, "Food", "expense", "2026-10-03")
    add_transaction(items, 20, "Food", "expense", "2026-10-04")
    add_transaction(items, 25, "Travel", "expense", "2026-10-04")
    add_transaction(items, 300, "Food", "expense", "2026-09-04")
    result = monthly_summary(items, 2026, 10)
    assert result["income"] == Decimal("1000")
    assert result["expenses"] == Decimal("85")
    assert result["balance"] == Decimal("915")
    assert result["expenses_by_category"] == {"Food": Decimal("60"), "Travel": Decimal("25")}


def test_empty_month_has_zero_totals():
    result = monthly_summary([], 2026, 10)
    assert result["income"] == result["expenses"] == result["balance"] == Decimal("0")
    assert result["expenses_by_category"] == {}


def test_summary_rejects_invalid_month():
    with pytest.raises(ValueError):
        monthly_summary([], 2026, 0)
