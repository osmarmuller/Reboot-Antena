#!/bin/bash
DATA=$(date +%d-%m-%y)
python3 /opt/scripts/unifi.py > /var/log/unifi/reboot-$DATA.log
find /var/log/unifi/reboot-* -mtime +7 -exec rm {} \;
