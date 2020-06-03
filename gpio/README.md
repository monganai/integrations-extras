# Agent Check: GPIO

## Overview

This check monitors [GPIO][1] through the Datadog Agent.

## Setup

Follow the instructions below to install and configure this check for an Agent running on a host. For containerized environments, see the [Autodiscovery Integration Templates][2] for guidance on applying these instructions.

### Installation

To install the GPIO check on your host:

1. Install the [developer toolkit](https://docs.datadoghq.com/developers/integrations/new_check_howto/#developer-toolkit) on any machine.
2. Run `ddev release build gpio` to build the package.
3. [Download the Datadog Agent](https://app.datadoghq.com/account/settings#agent).
4. Upload the build artifact to any host with an Agent andrun `datadog-agent integration install -w path/to/gpio/dist/<ARTIFACT_NAME>.whl`.

### Configuration

1. Edit the `gpio.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your gpio performance data. See the [sample gpio.d/conf.yaml][3] for all available configuration options.

2. [Restart the Agent][4].

### Validation

[Run the Agent's status subcommand][5] and look for `gpio` under the Checks section.

## Data Collected

### Metrics

See [metadata.csv][6] for a list of metrics provided by this check.

### Service Checks

GPIO does not include any service checks.

### Events

GPIO does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][7].

[1]: **LINK_TO_INTEGRATION_SITE**
[2]: https://docs.datadoghq.com/agent/autodiscovery/integrations
[3]: https://github.com/DataDog/integrations-core/blob/master/gpio/datadog_checks/gpio/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[6]: https://github.com/DataDog/integrations-core/blob/master/gpio/metadata.csv
[7]: https://docs.datadoghq.com/help
