"""
module for helper functions of validations
"""

from typing import Any

from pydantic_core import ErrorDetails


def pydantic_error_parser(errors: list[ErrorDetails]) -> dict[int | str, Any]:
    """
    Function to parse errors returned by pydantic and return those in a dict
    Params
    ------
    errors : list
        A list of errors in format of dict
        Example : [
                    {
                    'type': 'less_than_equal',
                    'loc': ('debt_score_emi_weightage',),
                    'msg': 'Input should be less than or equal to 100',
                    'input': 910, 'ctx': {'le': 100},
                    'url': 'https://errors.pydantic.dev/2.7/v/less_than_equal'
                    }
                ]
    Returns
    -------
    error_dict : dict
        A dict with parameter name where value is invalid as `key`, and error message as `value`
    """
    nested_errors: dict[int | str, Any] = {}

    for error in errors:
        loc = error["loc"]
        msg = error["msg"]

        current = nested_errors
        for key in loc[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]

        current[loc[-1]] = msg

    return nested_errors
