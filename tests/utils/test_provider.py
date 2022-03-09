import math
from typing import Any, Dict

from hypothesis import given, infer, settings

from rsserpent.utils import fetch_data
from tests.conftest import Times


async def provider(
    a: int, *, b: float, c: bool, d: int = 1, **_: Dict[str, Any]
) -> Dict[str, Any]:
    """Define an example data provider function for testing."""
    if c:
        return {"value": a + b + d}
    return {"value": a - b + d}


@settings(max_examples=Times.SOME)
@given(a=infer, b=infer, c=infer)
async def test_fetch_data(a: int, b: float, c: bool) -> None:
    """Test if `fetch_data` works properly with different kinds of parameters."""
    data = await fetch_data(provider, {"a": str(a)}, {"b": str(b), "c": str(c)})
    value = data["value"]
    if c:
        assert value == a + b + 1 or math.isnan(value)
    else:
        assert value == a - b + 1 or math.isnan(value)
