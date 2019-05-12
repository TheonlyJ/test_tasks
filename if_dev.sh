#!/bin/bash
for iface in $(ls /sys/class/net)
do
dev=$(cat /sys/class/net/$iface/device/device 2>/dev/null)
ven=$(cat /sys/class/net/$iface/device/vendor 2>/dev/null)
if [ $? -ne 0 ]
then
echo "$iface: no physical device"
continue
else
name=$(lspci -d $ven:$dev | sed -e  's/\(.*\):\(.*\): \(.*\)/\3/')
echo "$iface: $name"
fi
done
