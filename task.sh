#!/bin/bash
RUN_DIR="$( cd "$( dirname "$BASH_SOURCE[0]" )" && pwd )";
CMD="echo $RUN_DIR | sh $RUN_DIR/run.sh"
echo "0 7 */2 * *   root    $CMD" > /etc/cron.d/OpenWrt_configuration_backup;
/etc/init.d/cron reload;
