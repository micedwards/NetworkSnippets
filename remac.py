#!/bin/env python
import argparse

def convert(MACaddress):
    if MACaddress.rfind(':') > 0:
        lconvert = lambda mac: '.'.join(MACaddress.replace(':', '')[i:i+4] for i in range(0, 12, 4))
        return lconvert(MACaddress)
    elif MACaddress.rfind('-') > 0:
        lconvert = lambda mac: '.'.join(MACaddress.replace('-', '')[i:i+4] for i in range(0, 12, 4))
        return lconvert(MACaddress)
    elif MACaddress.rfind('.') > 0:
        lconvert = lambda mac: ':'.join(MACaddress.replace('.', '')[i:i+2] for i in range(0, 12, 2))
        return lconvert(MACaddress)
    else:
        return MACaddress

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("MACaddr",
                        help="MAC address to convert")
    args = parser.parse_args()
    if args.MACaddr is not None:
        print(convert(args.MACaddr))
    else:
        print("No MAC address provided")

if __name__ == "__main__":
    main()
