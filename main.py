
from tri import *

arendre = 7


# Ahoana ary ny fomba anaovana an'ito
# Mitovy amin'ny piece oa ito
# Satria mitady fotsiny hoe element 3 manana combinaison ilay izy 

def divisionBy2( value , systems ):
	array = []
	for i in range( 0 , len(systems) - 1 ):
		for j in range( i + 1 , len(systems) ):
			a = [ systems[i] , systems[j] ]
			if( systems[i] + systems[j] == value ):
				array.append(a)
				return a
	return array

def searchOne( value, systems ):

	for i in range( 0 , len(systems) ):
		if systems[i] == value:
			return systems[i]
	return []

def divisionByN( system, value , step ):
	if step == 1:
		return searchOne( value , system )
	if step == 2:
		return divisionBy2( value, system )
	else :
		for i in range(len(system)):
			newValue = value - system[i]
			k = step - 1
			currvalue = system[i]
			array = divisionByN( system[ i + 1 : ] , newValue, k )
			if array :
				return [currvalue] + array


	return []

def searchItem( array , target ):
	step = 1
	result = []
	while step <= target:
		result = divisionByN( array , target, step )
		if( len(result) > 0 ): return result
		step = step + 1
	return result

system = [ 2,6,1,3,1 , 5 ]
tri(system)
a = searchItem( system , 18 )
print(a)