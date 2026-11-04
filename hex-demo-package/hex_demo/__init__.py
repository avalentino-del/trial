"""hex_demo: a tiny package for testing Git package import in Hex."""

from .orders import clean_orders, load_sample_orders, summarize_by_region

__version__ = "0.1.0"
__all__ = ["clean_orders", "load_sample_orders", "summarize_by_region"]
