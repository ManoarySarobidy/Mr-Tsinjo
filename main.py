# Inona ilay atao
# Mitady hoe ahoana no manao ilay izy

def sort( arr, arr1, arr2 ):
	i = j = k = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arr[k] = arr1[i]
			i += 1
		else:
			arr[k] = arr2[j]
			j += 1
		k += 1
	
	while i < len(arr1):
		arr[k] = arr1[i]
		i += 1
		k += 1

	while j < len(arr2):
		arr[k] = arr2[j]
		j += 1
		k += 1

def mergeSort(arr):
    if len(arr) > 1:
	    mid = len(arr) // 2
	    sub_array1 = arr[:mid]
	    sub_array2 = arr[mid:]
	    mergeSort(sub_array1)
	    mergeSort(sub_array2)
	    sort( arr , sub_array1, sub_array2 ) 

def sum2( array , begin, sums , found):
	combination = []
	for i in range( begin , len(array) ):
		for j in range( i + 1 , len(array) ):
			if array[i] + array[j] == sums:
				combination.append( [ array[i] , array[j] ] )
				found[0] = True
	return combination

def sumK( array, sums, item, begin, combination, result , found):

	if( item == 2 ):
		result.append(sum2( array , begin, sums, found ))
	else:
		for i in range( begin, len(array) + 1 - item ):
			sumK( array, sums, item - 1, i + 1, combination + [array[i]], result, found )

def init( array , sums ):
	k = 2
	result = []
	found = [False]
	for k in range( 2 , len(array) ):
		sumK( array , sums, k ,0 , [] , result, found )
		if found[0] :
			break
	return result

array = [ 10 , 9, 5 , 7 , 8 , 3 , 2, 6 , 1 , 5 , 1 ]
mergeSort(array)
result = init( array , 10 )
print(result)