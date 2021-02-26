#!/bin/bash
BACKUP=/var/backup/OpenWrt
read -t 10 -p "输入项目文件位置：" RUN_DIR2
CMD="python3 $RUN_DIR2/run.py -c $RUN_DIR2/config.yaml"

# 创建目录
[ ! -d $BACKUP ] && mkdir -p $BACKUP
cd $BACKUP
$CMD
find ${BACKUP} -atime +60 -name "*.tar.gz" -exec rm -rf {} \;
