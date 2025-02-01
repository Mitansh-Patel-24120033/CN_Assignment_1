# CN_Assignment_1
This is the repository containing the files for assignment(1) of Computer Networks(2025) at IIT Gandhinagar.
Team Overview:
Mitansh Patel(24120033)
Gaurav Kumar(24120027)

Assignment Overview:-

This project involves developing a raw packet sniffer to analyze and compute various network metrics from a given pcap file. The assignment is divided into three parts:
Metrics and Plots: Extract and generate metrics from the pcap file.
Catch Me If You Can: Answer specific questions based on the pcap file.
Capture the Packets: Capture and analyze network packets using Wireshark.

Tools and Technologies:-

Programming Language: Python
Packet Replay Tool: tcpreplay
Packet Capture Tool: Wireshark

TCPREPLAY:
tcpreplay is an open-source suite of utilities that allows users to replay captured network traffic (from tools like tcpdump or Wireshark) back onto a network. It’s commonly used for testing the performance of network devices, intrusion detection systems, and security appliances by simulating real-world traffic. tcpreplay supports features like traffic rate control, packet editing, and multi-interface replay, making it versatile for both simple and complex network testing scenarios.

WIRESHARK:
Wireshark is a widely-used open-source network protocol analyzer that captures and displays network packets in real time. It allows users to inspect the details of various network protocols, troubleshoot network issues, and analyze security problems. With its powerful filtering and visualization tools, Wireshark is essential for network administrators, security analysts, and developers to diagnose and understand network behavior. It supports hundreds of protocols and runs on multiple platforms, including Windows, macOS, and Linux.

PREREQUISITES:-

OS:
Any linux distribution

Packages:
1) python3
2) pip
3) tcpreplay
4) jupyter
5) wireshark

ABOUT:-

The repository contains a Jupyter notebook file, which can be reviewed for testing.

[test1.sh] script will: 
Install required libraries via pip
Run the custon sniffer program
Display Matrics and Plots

[test2.sh] script will:
Run the tcpreplay tool at topspeed at user-inputted network interface and display its statistics.

[Part_01_02.py] python snipper program is also availabel to run independently.

INSTRUCTIONS:-

1) Clone this repository and add 1.pcap into the directory.
2) You can run custom sniffer program by executing test1.sh, run [$chmod +x test1.sh] to permit it, and execute it by[$./test1.sh].
3) You can run tcpreplay tool by running test2.sh, run [$chmod +x test2.sh] to permit it, and execute it by[$./test2.sh]. Input your network interface when asked.
4) You can overview Jupyter Notebook file i.e. [P01&P02.ipynb].
5) You can also custom run sniffer program by [$python3 Part_01_02.py]
