from typing import Any, Dict

from datadog_checks.base.stubs.aggregator import AggregatorStub
from datadog_checks.gpio import GpioCheck


def test_check(aggregator, instance):
    # type: (AggregatorStub, Dict[str, Any]) -> None
    check = GpioCheck('gpio', {}, [instance])
    check.check(instance)

    aggregator.assert_all_metrics_covered()
