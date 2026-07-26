from utils.formatter import format_currency
def format_currency(value):

    if abs(value) >= 1_000_000_000:
        return f"${value/1_000_000_000:.2f}B"

    if abs(value) >= 1_000_000:
        return f"${value/1_000_000:.2f}M"

    if abs(value) >= 1_000:
        return f"${value/1_000:.2f}K"

    return f"${value:,.0f}"