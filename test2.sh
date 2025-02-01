#!/bin/bash
echo -e "Please ensure you are on Linux platform, and have tcreplay installed\n"
echo -e "This script file will replay the packets of 1.pcap file at topspeed\n"
echo -e "Please enter a suitable nnetwork interface:"
read itf
sudo tcpreplay --intf1=$itf --stats=1 --topspeed 1.pcap
echo -e "\nYou can use this test script on multiple linux operated devices"
