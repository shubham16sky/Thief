from scapy.all import *

def packet_handler(packet):
    if packet.haslayer(ICMP):
        icmp_packet = packet.getlayer(ICMP)
        if icmp_packet.type == 8:  # ICMP Echo Request
            source = packet[IP].src
            if Raw in packet:
                data = packet[Raw].load.decode('utf-8')
                print(f'[x] FROM - [{source}] - {data}')
                
            else:
                print(f'[x] FROM - [{source}]')
                print('[x] No payload data')

def receive_icmp_data(interface):
    print('[x] READY TO RECEIVE')
    print('[x] PRESS CTRL+C TO INTERRUPT')
    sniff(filter='icmp', prn=packet_handler, store=0,iface=interface)

if __name__ == '__main__':
    receive_icmp_data(interface='lo')
