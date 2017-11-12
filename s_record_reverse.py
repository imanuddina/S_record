import sys
import csv
ADDR_W = 8
srec_file = 'ip4_UDP_2.s'
rev_file = 'ip4_UDP_2.pkt'


def onec(b):
    byte = [b[i:i+2] for i in xrange(0, len(b), 2)]
    sum=0
    # Sum all bytes starts from first byte
    for i in range(len(byte)):
        sum+=int(byte[i], 16)
    # First complement
    cs = (sum ^ 0xFF) & 0xFF
    return '%0.2X' % cs

filereader = open(srec_file,'r')
frame=''
for row in filereader:
    
    rec = row.strip()
    if('S0' == rec[0:2] or 'S7' == rec[0:2]): continue
    # Verifying content checksum
    bl = rec[2:4]
    ad = rec[4:12]
    byte_len = int(rec[2:4], 16)-5
    pos = 4 + ADDR_W
    pos_last = pos+(byte_len<<1)
    pkt = rec[pos:pos_last]
    cs = rec[pos_last:pos_last+2]
    
    if(cs != onec(bl+ad+pkt)):
        print 'corrupted pkt/csum'
    print rec[0:2], byte_len, ad, cs #pkt
    frame += pkt
rpos=0
print frame
filereader.close()

