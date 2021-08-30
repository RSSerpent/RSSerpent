import inspect
from inspect import Parameter
from typing import Any, Awaitable, Callable, Dict


ProviderFn = Callable[..., Awaitable[Dict[str, Any]]]


def convert(value: str, type_: type) -> Any:
    """Convert string `value` to type `type_`."""
    if type_ is bool:
        return value.lower() in ("1", "t", "true", "y", "yes")
    return type_(value)


async def fetch_data(
    provider: ProviderFn, view_args: Dict[str, Any], qs: Dict[str, str]
) -> Any:
    """Fetch data by using the data provider function.

    We first inspect the signature of the `provider` function to determine what
    parameters it needs. We then find values for these parameters from `view_args` &
    `qa`. Finally we invoke `provider(*args, **kwds)` and return the fetched data.

    Args:
        provider: The data provider function.
        view_args: `request.view_args`, arguments parsed from the route.
        qs: `request.args`, arguments parsed from the query string, but deduplicated.

    Returns:
        The data fetched by the `provider` function.

    Raises:
        NotImplementedError:do not use positional-only arguments in `provider`.
    """
    kwds = {}
    for parameter in inspect.signature(provider).parameters.values():
        # ignore `*args` & `**kwds` arguments
        if parameter.kind in (Parameter.VAR_POSITIONAL, Parameter.VAR_KEYWORD):
            continue
        parameter_value = look_up_parameter_value(parameter, view_args, qs)
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
    parameter: Parameter, view_args: Dict[str, Any], qs: Dict[str, str]
) -> Any:
    """Look up value for a specific parameter from `view_args` & `qs`.

    Args:
        parameter: A parameter of some data provider function (`ProviderFn`).
        view_args: `request.view_args`, arguments parsed from the route.
        qs: `request.args`, arguments parsed from the query string, but deduplicated.

    Returns:
        The value for the parameter, `None` if not found.
    """
    value = None
    # look for `parameter.name` in `view_args`
    if parameter.name in view_args:
        value = view_args[parameter.name]
        if isinstance(value, str):
            value = convert(value, parameter.annotation)
    # looking for `parameter.name` in `qs`
    elif parameter.name in qs:
        value = convert(qs[parameter.name], parameter.annotation)
    return value
