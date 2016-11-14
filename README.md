# StatusCake_monitor
a services monitoring system that updates "Push" Tests on StatusCake.com
StatusCake PUSH depends on [my own GitHub "infra_monitor" repository](https://github.com/Fclem/infra_monitor)
This uses  StatusCake.com along with a PUSH scheme to update test instead of updating check on a status change basis.

## How to start :
bash :
```bash
git clone https://github.com/Fclem/StatusCake_monitor.git && cd StatusCake_monitor && git clone https://github.com/Fclem/infra_monitor.git
vim config.ini
./__init__.py
```

fish :
```shell
git clone https://github.com/Fclem/StatusCake_monitor.git; and cd StatusCake_monitor; and git clone https://github.com/Fclem/infra_monitor.git
vim config.ini
./__init__.py
```

***documentation from top-level repository***

Checks are loaded from `config.ini`

## Currently supported checks types :
 * `url` : if HTTP GET to *url* returns HTTP 200
 * `tcp` : if connection to TCP *host port* is successful
 * `ping` : if remote *host* replies to ICMP ping (through system's ping command)

## To be supported checks types :
 * `docker` : if a named docker container is running
