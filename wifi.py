from scapy.all import *
import re

PROBE_REQUEST_TYPE=0
PROBE_REQUEST_SUBTYPE=4
iterations=0

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type==PROBE_REQUEST_TYPE and pkt.subtype == PROBE_REQUEST_SUBTYPE:
            PrintPacket(pkt)
arr_mac = {}
def PrintPacket(pkt):
    global iterations
    iterations += 1

    print "A: %d" % iterations

    try:
        extra = pkt.notdecoded
    except:
        extra = None
    if extra!=None:
        signal_strength = -(256-ord(extra[-4:-3]))
    else:
        signal_strength = -100
    mac = pkt.addr2
    signal = signal_strength.__str__()
    probe = pkt.getlayer(Dot11ProbeReq).info
    arr_mac[mac] = signal
#    print arr_mac
    if iterations > 1000:
        f = open('text.txt', 'w')
        a = arr_mac.keys()
       # print a
        for mac in a:
            sig = arr_mac[mac]
            f.write(mac + '_' + sig.replace('-','') +'\n' )
        f.close()
        iterations = 0
        arr_mac.clear()

def main():
    sniff(iface=sys.argv[1],prn=PacketHandler)

if __name__=="__main__":
    main()
