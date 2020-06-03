import os
import time
from datadog_checks.base import AgentCheck


class GpioCheck(AgentCheck):
    def check(self, instance):
        # the following try/except block will make the custom check compatible with any Agent version
        try:
            # first, try to import the base class from new versions of the Agent...
            from datadog_checks.base import AgentCheck
        except ImportError:
             # ...if the above failed, the check is running in Agent version < 6.6.0
            from checks import AgentCheck
        self.gauge('system.temp.celsius', get_temp())
        self.gauge('system.temp.fahrenheit', get_temp() * (9/5) + 32)


def get_temp():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    return (float(temp)/1000)


       