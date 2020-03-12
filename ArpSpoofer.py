import argparse
import scapy


def parse_command():
    ap = argparse.ArgumentParser(description="Spoof ARP tables")
    ap.add_argument('-i', '--iface', nargs=1, help='Interface you wish to use')
    ap.add_argument('-s', '--src', nargs=1, help='The address you want for the attacker')
    ap.add_argument('-d', '--delay', nargs=1, type=int, default=0, help='Delay (in seconds) between messages')
    ap.add_argument('-gw', action='store_true', default=False, help='should GW be attacked as well')
    ap.add_argument('-t', '--target', nargs=1, help='IP of target')
    return ap.parse_args()


def main():
    pass


if __name__ == '__main__':
    args = parse_command()
    print(args)
    main()
