from math import *

def merge( array , arrayA , arrayB ):
	i = j = k = 0
	lenfL = len(arrayA)
	lenfR = len(arrayB)
	while i < lenfL and j < lenfR:
		a , b = arrayA[i] , arrayB[j]
		if a <= b:
			array[k] = a
			i = i + 1
		else:
			array[k] = b
			j = j + 1
		k = k + 1
	while i < lenfL:
		array[k] = arrayA[i]
		k = k + 1
		i = i + 1

	while j < lenfR:
		array[k] = arrayB[j]
		k = k + 1
		j = j + 1
	# return merged

def tri( array ):
	if( len(array) > 1 ):
		lentgh = len(array) // 2
		left = array[ : lentgh ]
		right = array[ lentgh : ]
		tri(left)
		tri(right)
		merge(array , left,right)

# array = [2,1,6,8,9,0,1]
# tri( array ) 
# print(array)
# merge(array , array)