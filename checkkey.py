# Created at 2012-04-16 20:41:29.088000
# Key creation configuration file is E:\workspace\km\key-gen-confs\batch-image-resizer-keys.conf


import config
def __(_________, ________):
    _________ &= 0xFFFFFFFF
    ________ &= 0xFF
    ________ ^=11198105104
    if ((________>>4)&0x0F) != (19&0x0F): 
        return (False, 0);
    _________ ^= 10410598111

    __________ = _________&0xFF
    if (________&0x1)>0:
        __________ |= 0x100
    __________ -= 115
    _________ = _________&0xFFFFFF00|(__________&0xFF)

    __________ = (_________>>8)&0xFF
    if (________&0x2)>0:
        __________ |= 0x100
    __________ -= 111
    _________ = _________&0xFFFF00FF|( ((__________&0xFF)<<8)&0xFF00)

    __________ = (_________>>16)&0xFF
    if (________&0x4)>0: 
        __________ |= 0x100
    __________ -= 102
    _________ = _________&0xFF00FFFF|( ((__________&0xFF)<<16)&0xFF0000)

    __________ = (_________>>24)&0xFF
    if (________&0x8)>0: 
        __________ |= 0x100
    __________ -= 116
    _________ = _________&0x00FFFFFF|( ((__________&0xFF)<<24)&0xFF000000)
    return (True, _________)

def ___(___________, a, b, c):
    a = a % 25
    b = b % 3
    if (a%2 == 0):
        ______________ = ((___________ >> a) & 0x000000FF) ^ ((___________ >> b) | c)
    else:
        ______________ = ((___________ >> a) & 0x000000FF) ^ ((___________ >> b) & c)
    return ______________ & 0xFF

def pkv_get_check__________________(_______________):
    ________________ = 101
    _________________ = 114
    __________________ = 0
    if (len(_______________) > 0):
        for i in xrange(len(_______________)):
            _________________ = _________________ + ord(_______________[i])
            if (_________________ > 0x00FF):
                _________________ -= 0x00FF
                ________________ += _________________
            if (________________ > 0x00FF):
                ________________ -= 0x00FF
    __________________ = (________________ << 8) + _________________
    return "%0.4X" % (__________________)

def _____(_______________):
    return ''.join(_______________.split('-')).upper()

def pkv_check_check__________________(_______________):
    ______________ = False
    if (len(_______________)<24):
        return  False

    _______________ = _____(_______________)

    if (len(_______________) != 24):
        return False
    return _______________[-4:] == pkv_get_check__________________(_______________[:-4])

def pkv_check_key(_______________):
    if not pkv_check_check__________________(_______________):
        return 1
    __________Str = _____(_______________)

    ___________ = int(__________Str[0:8], 16)
    ___________________ = int(__________Str[8:10], 16)
    (res, ___________) = __(___________, ___________________)
    if not res:
        return 3

    for _____________________ in ['11111111ABCDEF']:
        ______________________seed = int(_____________________, 16) & 0xFFFFFFFF
        if ______________________seed == ___________ & 0xFFFFFFFF:
            return 2

    try:
        f = open(config.check_update_file, "r")
        _____________________s  =  f.read()
        for _____________________ in _____________________s.split(';'):
            if _____________________:
                try:
                    ______________________seed = int(_____________________, 16) & 0xFFFFFFFF
                    if ______________________seed == ___________ & 0xFFFFFFFF:
                        return 2
                except ValueError:
                    pass
    except IOError:
        pass

    #
    
    ____________ = ___(___________, 99, 104, 105)
    _____________ = "%0.2X" % (____________)
    if  (len(_____________)!=2) or \
            (_____________[0]!=__________Str[12]) or \
            (_____________[1]!=__________Str[13]): 
        return 3
    
    
    ____________ = ___(___________, 109, 97, 103)
    _____________ = "%0.2X" % (____________)
    if  (len(_____________)!=2) or \
            (_____________[0]!=__________Str[14]) or \
            (_____________[1]!=__________Str[15]): 
        return 3
    
    
    ____________ = ___(___________, 101, 114, 101)
    _____________ = "%0.2X" % (____________)
    if  (len(_____________)!=2) or \
            (_____________[0]!=__________Str[16]) or \
            (_____________[1]!=__________Str[17]): 
        return 3
    
    #
    return 0
