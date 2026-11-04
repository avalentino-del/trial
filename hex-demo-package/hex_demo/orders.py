from pathlib import Path

import pandas as pd

# Resolve the bundled data file relative to this module, so it works whether the
# repo is added to sys.path or the package is pip-installed.
DATA_DIR = Path(__file__).parent / "data"


def load_sample_orders() -> pd.DataFrame:
    """Load the sample orders CSV that ships inside the package."""
    return pd.read_csv(DATA_DIR / "sample_orders.csv", parse_dates=["order_date"])


def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Drop rows with missing amounts, standardize region names, add a revenue tier."""
    out = df.dropna(subset=["amount"]).copy()
    out["region"] = out["region"].str.strip().str.title()
    out["tier"] = pd.cut(
        out["amount"],
        bins=[0, 100, 500, float("inf")],
        labels=["small", "medium", "large"],
    )
    return out


def summarize_by_region(df: pd.DataFrame) -> pd.DataFrame:
    """Total revenue and order count per region, sorted by revenue."""
    return (
        df.groupby("region", as_index=False)
        .agg(revenue=("amount", "sum"), orders=("order_id", "count"))
        .sort_values("revenue", ascending=False)
        .reset_index(drop=True)
    )
