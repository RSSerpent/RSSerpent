import inspect
from inspect import Parameter
from typing import Any, Dict

from ..models import ProviderFn


def convert(value: str, type_: type) -> Any:
    """Convert string `value` to type `type_`."""
    if type_ is bool:
        return value.lower() in ("1", "t", "true", "y", "yes")
    return type_(value)


async def fetch_data(
    provider: ProviderFn, path_params: Dict[str, Any], query_params: Dict[str, str]
) -> Any:
    """Fetch data by using the data provider function.

    We first inspect the signature of the `provider` function to determine what
    parameters it needs. We then find values for these parameters from `path_params` &
    `query_params`. Finally we invoke `provider(**kwds)` and return the fetched data.

    Args:
        provider: The data provider function.
        path_params: `request.path_params`, arguments parsed from the route path.
        query_params: `request.query_params`, arguments parsed from the query string,
            but deduplicated.

    Returns:
        The data fetched by the `provider` function.

    Raises:
        NotImplementedError: do not use positional-only arguments in `provider`.
    """
    kwds = {}
    for parameter in inspect.signature(provider).parameters.values():
        # ignore `*args` & `**kwds` arguments
        if parameter.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
            continue
        parameter_value = look_up_parameter_value(parameter, path_params, query_params)
        if parameter_value is None:
            continue
        # handle positional-or-keyword & keyword-only arguments
        elif parameter.kind in (
            Parameter.POSITIONAL_OR_KEYWORD,
            Parameter.KEYWORD_ONLY,
        ):
            kwds[parameter.name] = parameter_value
        # do not use positional-only arguments
        # TODO: document this behavior
        else:
            raise NotImplementedError()  # pragma: no cover
    return await provider(**kwds)


def look_up_parameter_value(
    parameter: Parameter, path_params: Dict[str, Any], query_params: Dict[str, str]
) -> Any:
    """Look up value for a specific parameter from `path_params` & `query_params`.

    Args:
        parameter: A parameter of some data provider function (`ProviderFn`).
        path_params: `request.path_params`, arguments parsed from the route.
        query_params: `request.query_params`, arguments parsed from the query string,
            but deduplicated.

    Returns:
        The value for the parameter, `None` if not found.
    """
    value = None
    # look for `parameter.name` in `path_params`
    if parameter.name in path_params:
        value = path_params[parameter.name]
        if isinstance(value, str):
            value = convert(value, parameter.annotation)
    # looking for `parameter.name` in `query_params`
    elif parameter.name in query_params:
        value = convert(query_params[parameter.name], parameter.annotation)
    return value
