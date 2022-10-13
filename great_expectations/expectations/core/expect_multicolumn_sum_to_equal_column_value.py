from typing import Optional

from great_expectations.core import ExpectationConfiguration
from great_expectations.expectations.expectation import MulticolumnMapExpectation
from great_expectations.expectations.util import render_evaluation_parameter_string
from great_expectations.render.renderer.renderer import renderer

class ExpectMulticolumnSumToEqualColumnValue(MulticolumnMapExpectation):
    """
    Expect that the sum of row values is equal to the value of an other row.
    Summing only values in columns specified in column_list, and equal to the specific column value, sum_column.

    Args:
            column_list (tuple of list): Set of columns to be checked
            sum_column (tuple) : Expected sum column

    Keyword Args:
        ignore_row_if (str): "all_values_are_missing", "any_value_is_missing", "never"

    Other Parameters:
        result_format (str or None): \
            Which output mode to use: `BOOLEAN_ONLY`, `BASIC`, `COMPLETE`, or `SUMMARY`.
        include_config (boolean): \
            If True, then include the expectation config as part of the result object. \
        catch_exceptions (boolean or None): \
            If True, then catch exceptions and include them as part of the result object. \
        meta (dict or None): \
            A JSON-serializable dictionary (nesting allowed) that will be included in the output without modification.

    Returns:
        An ExpectationSuiteValidationResult
    """

    # This dictionary contains metadata for display in the public gallery
    library_metadata = {
        "maturity": "experimental",
        "tags": [
            "core expectation",
            "column aggregate expectation",
        ],
        "contributors": ["@AntoineTSIO"],
        "requirements": [],
        "has_full_test_suite": False,
        "manually_reviewed_code": False,
    }