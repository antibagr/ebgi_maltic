import sys

import random

def nlogn_median(l):
	l = sorted(l)
	if len(l) % 2 == 1:
		return l[ round(len(l)/2) ]
	else:
		return 0.5 * l[ len(l) / 2 - 1] + l[ len(l) / 2 ]

def quickselect_median(l,pivot_fn=random.choice):
	if len(l) % 2 == 1:
		return quickselect(l,len(l)/2,pivot_fn)
	else:
		return 0.5 * (quickselect(l, len(l) / 2 - 1, pivot_fn ) +
					(quickselect(l, len(l) / 2, pivot_fn )))

def quickselect(l,k,pivot_fn):

	if len(l) == 1:
		assert k == 0
		return l[0]

	pivot = pivot_fn

	lows = [el for el in l if el < pivot]
	highs = [el for el in l if el > pivot]
	pivots = [el for el in l if el == pivot]

	if k < len(lows):
		return quickselect(lows,k,pivot_fn)
	elif k < len(lows) + len(pivots):
		return pivots[0]
	else:
		return quickselect(highs,k - len(lows) - len(pivots),pivot_fn)




