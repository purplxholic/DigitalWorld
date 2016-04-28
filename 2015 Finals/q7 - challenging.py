import math
def countNumOpenLocker(K):
    lockers = ['c'] * K

    length = len(lockers)
    #first pass
    for i in range(length):
        lockers[i] = 'o'

    #prof one, i is pass, m is locker number
    # for i in range(1,K+1):
    #     for m in range(1,K+1):
    #         if m % i == 0:
    #             if lockers[m] == 'o':
    #                 lockers[m] = 'c'
    #             else:
    #                 lockers[m] = 'o'

    #try again
    #second pass onwards

    # for going in range(2,K):
    #     print going
    #     for i in range(length):
    #         if i%going == 0:
    #             if lockers[i] == 'o':
    #                 lockers[i] = 'c'
    #             else:
    #                 lockers[i] = 'o'
    #             print lockers

    #nic's one
    # count = 0
    # for i in range(1,K):
    #     if (math.sqrt(i)).is_integer() == True:
    #         count +=1
    # return count

    #or
    return int(math.floor(K**0.5))

print countNumOpenLocker(2000)