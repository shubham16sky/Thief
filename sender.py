from scapy.all import *
import sys

#function to send message to destination address using ICMP protocol. Limit if data is 32 characters. 
def send_message(dest_addr,text):
    if len(text) > 32:
        print(f'--> Data size is greater than 32 characters')
        sys.exit(1)
    
    packet = IP(dst=dest_addr)/ICMP()/text
    send(packet)
    print(f'--> Sent {text} to {dest_addr}')

if __name__ == '__main__':
    if len(sys.argv) !=3:
        print(f'Usage : python3 sender.py [destination_addr] [text]')
        sys.exit(1)
    
    destination_addr = sys.argv[1]
    text = sys.argv[2]

    send_message(dest_addr=destination_addr,text=text)


    


