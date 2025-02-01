import time
import matplotlib.pyplot as plt
from scapy.all import *
from collections import defaultdict
import gc
import re

# Load 1.pcap file
start_load = time.time()
file = PcapReader("1.pcap")
#Read all packets
packets=file.read_all()
end_load = time.time()
print(f"Loaded {len(packets)} packets in {end_load - start_load:.3f} seconds")
print("Packets loaded, now sniffing...")

# Metrics
tdata = 0
packet_sizes = []
pairs = set()
src_fl = defaultdict(int)
dst_fl = defaultdict(int)
data_by_pair = defaultdict(int)
total_packets = 0

email_subject = None
recipient_email = None
dns_server = None
resolved_ip = None

# Sniff packets
sniff_start=time.time()
for pac in packets:
    #Only check packets with IP header
    if pac.haslayer("IP"):
        src_ip = pac["IP"].src
        dst_ip = pac["IP"].dst
        src_port = None
        dst_port = None
        
        if pac.haslayer("TCP"):
            src_port = pac["TCP"].sport
            dst_port = pac["TCP"].dport
        elif pac.haslayer("UDP"):
            src_port = pac["UDP"].sport
            dst_port = pac["UDP"].dport
        
        ip_port_pair = (f"{src_ip}:{src_port}", f"{dst_ip}:{dst_port}")
        p_size = len(pac)
        tdata += p_size
        packet_sizes.append(p_size)
        pairs.add(ip_port_pair)
        
        # Update source and destination flows
        src_fl[src_ip] += 1
        dst_fl[dst_ip] += 1
        
        data_by_pair[ip_port_pair] += p_size
        total_packets += 1

        #Part 02 Questions
        #Q1 & Q2
        if pac.haslayer("TCP") and (pac["TCP"].sport == 25 or pac["TCP"].dport == 25):  # SMTP traffic
            raw_data = bytes(pac.payload)
            pattern = f"Subject:(.*?)(?:\n|$)"
            match=re.search(pattern,raw_data.decode(errors="ignore"))
            if match:
                email_subject=match.group(1).strip()
            pattern = f"RCPT TO:(.*?)(?:\n|$)"
            match=re.search(pattern,raw_data.decode(errors="ignore"))
            if match:
                recipient_email=match.group(1).strip()
        #Q3 & Q4
        if pac.haslayer("DNS") and pac["DNS"].qr == 1:  # DNS Response
            for i in range(pac["DNS"].ancount):
                if b"routerswitches.com" in pac["DNS"].an[i].rrname:
                    resolved_ip=pac['DNS'].an[i].rdata
            if pac["DNS"].qd and pac["DNS"].qd.qname and pac["DNS"].qd.qname.decode().strip(".") == "routerswitches.com":
                dns_server = pac[IP].src

        if total_packets % 100000 == 0:
            print(f"Sniffed {total_packets} packets")
sniff_end=time.time()

# Find the pair with the most data transferred
most_data_pair = max(data_by_pair.items(), key=lambda x: x[1], default=(None, 0))
# Calculate speed metrics
duration = sniff_end - sniff_start
pps = total_packets / duration  # Packets per second
mbps = (tdata * 8) / (duration * 1000000)  # Convert bytes to bits and scale to Mbps

del packets
file.close()
gc.collect()

# Metrics Results
print("\nSniffing Metrics after loading .pcap into memory...")
print(f"\nTotal Data Transferred: {tdata} bytes")
print(f"\nTotal Packets(with IP layer): {total_packets}")
print(f"\nMin Packet Size: {min(packet_sizes) if packet_sizes else 0} bytes")
print(f"\nMax Packet Size: {max(packet_sizes) if packet_sizes else 0} bytes")
print(f"\nAvg Packet Size: {sum(packet_sizes) / len(packet_sizes) if packet_sizes else 0:.2f} bytes")
print(f"\nUnique Source-Destination Pairs: {len(pairs)}")
print(f"\nSource IP Flows: {dict(src_fl)}")
print(f"\nDestination IP Flows: {dict(dst_fl)}")
print(f"\nCapture Duration: {duration:.3f} seconds")
print(f"\nPackets Per Second (PPS): {pps:.3f}")
print(f"\nMegabits Per Second (Mbps): {mbps:.3f}")
print(f"\nSource-Destination Pair with Most Data: {most_data_pair[0]} ({most_data_pair[1]} bytes)")

# Plot packet size distribution
plt.hist(packet_sizes, bins=20, color='blue', edgecolor='black')
plt.title('Packet Size Distribution')
plt.xlabel('Packet Size (bytes)')
plt.ylabel('Frequency')
plt.show()

print("\nPart 02 Answers:")
print(f"Email Subject: {email_subject}")
print(f"Recipient Email: {recipient_email}")
print(f"Resolved IP for routerswitches.com: {resolved_ip}")
print(f"DNS Server used: {dns_server}")

exit()
