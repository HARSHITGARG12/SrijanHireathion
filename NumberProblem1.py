def mySort1(Arr):
	l = len(Arr)
	i = 0
	j = 0
	while i < l:
		j = 0
		while j < l-1:
			if Arr[j]+Arr[j+1] > Arr[j+1]+Arr[j]:
				t1 = Arr[j]
				Arr[j] = Arr[j+1]
				Arr[j+1] = t1
			j = j+1				
		i = i+1					
	return Arr	
	
				
t = int(raw_input().strip())
for i in range(t):
	l = int(raw_input())
	Arr = map(str, raw_input().strip().split(' '))
	#print sorted(Arr)
	#Arr = sorted(Arr)
	#print sorted(Arr, cmp=mySort)
	print ''.join( i for i in mySort1(Arr))
