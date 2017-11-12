import sys
pkt = ('0015582E90010015582E800108004500007E000000004011746A010101010202'
       '020250016006006A1D0B000140005029F900021D0001C0A88001600E00000000'
       '0000000000000000000000000000000000000000000000000000000000000000'
       '0000000000000000000000000000000000000000000000000000000000000000'
       '000000000000000000000000')
print len(pkt)/2

rpos=0

def onec(b):
    byte = [b[i:i+2] for i in xrange(0, len(b), 2)]
    sum=0
    # Sum all bytes starts from first byte
    for i in range(len(byte)):
        sum+=int(byte[i], 16)
    # First complement
    cs = (sum ^ 0xFF) & 0xFF
    return '%0.2X' % cs

def limiter():

    bl = '05' # byte length
    ad = '%0.8X' % 0 # address
    
    return (bl + ad + onec(bl+ad))
    


print 'S0' + limiter() # start
l = len(pkt)
while(l>=0):
    s = pkt[rpos:rpos+64]
    #print s
    if(l>32):
       bl = '%0.2X' % (32+5)
       ad = '%0.8X' % (rpos/2)
       print 'S3' + '25' + ad + s + onec(bl+ad+s)
    else:
       bl = '%0.2X' % (l/2+5)
       ad = '%0.8X' % (rpos/2)
       print 'S3' + bl + ad  + s + onec(bl+ad+s)
       
    l-=64;
    rpos+=64
print 'S7' + limiter() # end

