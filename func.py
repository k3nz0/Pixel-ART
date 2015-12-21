def twoMaxs(lnp):
	"""
		Return 0-based index of the two max values
	"""
	index1 = 0
	index2 = 0
	cnt = 0
	maxArea = 0
	maxArea2 = 0
	for (ex, ey, ew, eh) in lnp:
		if(ew * eh >= maxArea):
			index1 = cnt
			maxArea = ew * eh
		cnt += 1
	

	cnt = 0
	for (ex, ey, ew, eh) in lnp:
		if(index1 == cnt):
			cnt += 1
			continue
		if(ew * eh >= maxArea2):
			index2 = cnt
			maxArea2 = ew * eh
		cnt +=1
	
	return (index1, index2)

def abs(x):
	if(x >= 0):
		return x
	else:
		return -x