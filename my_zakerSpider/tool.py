import time


def Timestamp():
    '''
    nowtime：当前时间戳(float)
    beforetime：之前的时间戳(int)
    :return: nowtime,beforetime
    '''
    nowtime = round(time.time(),3)
    beforetime = int(float(nowtime-181769))
    return nowtime,beforetime