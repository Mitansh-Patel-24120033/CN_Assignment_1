**# CN_Assignment_1**<br>

This is the repository containing the files for assignment(1) of Computer Networks(2025) at IIT Gandhinagar.<br>

Team Overview:<br>
Mitansh Patel(24120033)<br>
Gaurav Kumar(24120027)<br>

**Assignment Overview:-**<br>

This project involves developing a raw packet sniffer to analyze and compute various network metrics from a given pcap file. The assignment is divided into three parts:<br>
Metrics and Plots: Extract and generate metrics from the pcap file.<br>
Catch Me If You Can: Answer specific questions based on the pcap file.<br>
Capture the Packets: Capture and analyze network packets using Wireshark.<br>

**Tools and Technologies:-**<br>

Programming Language: Python<br>
Packet Replay Tool: tcpreplay<br>
Packet Capture Tool: Wireshark<br>

**TCPREPLAY:**<br>
tcpreplay is an open-source suite of utilities that allows users to replay captured network traffic (from tools like tcpdump or Wireshark) back onto a network. It’s commonly used for testing the performance of network devices, intrusion detection systems, and security appliances by simulating real-world traffic. tcpreplay supports features like traffic rate control, packet editing, and multi-interface replay, making it versatile for both simple and complex network testing scenarios.<br>

**WIRESHARK:**<br>
Wireshark is a widely-used open-source network protocol analyzer that captures and displays network packets in real time. It allows users to inspect the details of various network protocols, troubleshoot network issues, and analyze security problems. With its powerful filtering and visualization tools, Wireshark is essential for network administrators, security analysts, and developers to diagnose and understand network behavior. It supports hundreds of protocols and runs on multiple platforms, including Windows, macOS, and Linux.<br>

**PREREQUISITES:-**<br>

OS:<br>
Any linux distribution<br>

Packages:<br>
1) python3
2) pip
3) tcpreplay
4) jupyter
5) wireshark

**ABOUT:-**<br>

Part 1:<br>
This assignment is aimed at building a custom sniffer using any preferred language, and compare its metrics to that of tcpreplay tool.

Part 2:<br>
Much information from packets was extracted to answer basc question mean for 1.pcap file
The repository contains a Jupyter notebook file, which can be reviewed for testing.

Part 3:<br>
Via the use of Wireshark tool, packets were captures and analzsed.
Many sites were visited, and their attributes were captured.
Browser's inspect feature was used to capture the performance metrics of the websites.

[test1.sh] script will: <br>
Install required libraries via pip<br>
Run the custon sniffer program<br>
Display Matrics and Plots<br>

[test2.sh] script will:<br>
Run the tcpreplay tool at topspeed at user-inputted network interface and display its statistics.<br>

[Part_01_02.py] python snipper program is also availabel to run independently.<br>

**INSTRUCTIONS:-**<br>

1) Clone this repository and add 1.pcap into the directory.
2) You can run custom sniffer program by executing test1.sh, run [$chmod +x test1.sh] to permit it, and execute it by[$./test1.sh].
3) You can run tcpreplay tool by running test2.sh, run [$chmod +x test2.sh] to permit it, and execute it by[$./test2.sh]. Input your network interface when asked.
4) You can overview Jupyter Notebook file i.e. [P01&P02.ipynb].
5) You can also custom run sniffer program by [$python3 Part_01_02.py]
