#!/usr/bin/python3
"""Performs prime game"""

def isWinner(x, nums):
    """Function that performs prime game"""
    if not nums or x < 1:
        return None
        n = max(nums)
        filt = [True for _ in range(max(n + 1, 2))]
        for i in range(2, int(pow(n, 0.5)) + 1):
            if not filt[i]:
                continue
            for j in range(i * i, n + 1, i):
                filt[j] = False
        filt[0] = filt[1] = False
        d = 0
        for i in range(len(filt)):
            if filt[i]:
                d += 1
            filt[i] = d
        plyr1 = 0
        for n in nums:
            plyr1 += filt[n] % 2 == 1
        if plyr1 * 2 == len(nums):
            return None
        if plyr1 * 2 > len(nums):
            return "Maria"
        return "Ben"