"""Monthly income and spending summaries (Feature C)."""

from decimal import Decimal


def monthly_summary(transactions, year, month):
    """Summarize income, expenses, balance, and expense totals by category."""
    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12")
    if year < 1:
        raise ValueError("year must be positive")

    selected = [t for t in transactions if t.when.year == year and t.when.month == month]
    income = sum((t.amount for t in selected if t.kind == "income"), Decimal("0"))
    expenses = sum((t.amount for t in selected if t.kind == "expense"), Decimal("0"))
    by_category = {}
    for transaction in selected:
        if transaction.kind == "expense":
            by_category[transaction.category] = by_category.get(transaction.category, Decimal("0")) + transaction.amount
    return {
        "year": year,
        "month": month,
        "income": income,
        "expenses": expenses,
        "balance": income - expenses,
        "expenses_by_category": dict(sorted(by_category.items(), key=lambda item: item[0].casefold())),
    }
