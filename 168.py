def GetMissedItem (arr):
	i = 0
	d = (arr[len(arr) - 1] - arr[0]) / (len(arr))
	while (i < len(arr) - 1):
		if ((arr[i] + d) != arr[i+1]):
			return (arr[i] + d)
		i+=1
