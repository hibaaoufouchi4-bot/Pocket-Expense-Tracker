"""Monthly category budget calculations (Feature B)."""

from decimal import Decimal, InvalidOperation


def budget_status(transactions, category, limit, year, month):
    """Return spending, limit, remaining amount, and whether the limit is met."""
    try:
        budget = Decimal(str(limit))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("limit must be a valid number") from None
    if not budget.is_finite() or budget <= 0:
        raise ValueError("limit must be greater than zero")
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")
    if year < 1:
        raise ValueError("year must be positive")

    target = category.strip().casefold()
    if not target:
        raise ValueError("category cannot be empty")

    spent = sum(
        (t.amount for t in transactions
         if t.kind == "expense" and t.category.casefold() == target
         and t.when.year == year and t.when.month == month),
        Decimal("0"),
    )
    remaining = budget - spent
    return {
        "category": category.strip(),
        "spent": spent,
        "limit": budget,
        "remaining": remaining,
        "within_budget": spent <= budget,
    }
