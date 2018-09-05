#!/usr/bin/env python3

###Class implementation of of a hashtable map.
import unittest
import string

def myhash(inp_str, size):
	#print('hashing '+inp_str)
	sum = 0
	for c in inp_str:
		#print('value of '+c+' is: '+str(ord(c)))
		sum += ord(c)
		#print(sum)
	#print('final value of sum '+str(sum))
	return sum%size

#linear probing to avoid collisions for now. simply hash and return the value plus 3 mod size.
#chaining can be done with array within array since python takes care of it for ya :).

#exception testing???
class Error(Exception):
   """Base class for other exceptions"""
   pass
class NoSpaceError(Error):
	"""Raised when inserting new key but no space to insert"""
	pass
class NotStringError(Error):
	"""Raised when trying to insert a non string key"""
	pass
class NotInHashTable(Error):
	"""Raised when key is not present in HashTable"""
	pass


class hashtable:
	def __init__(self,size):
		self.size = size
		self.data = [None]*size 




	def put(self,key,data):
		hashedValue = myhash(key,self.size)
		inserted = False
		if isinstance(key,str):
			#insert if empty position.
			if self.data[hashedValue] == None:
				self.data[hashedValue] = [(key,data)]

			elif self.data[hashedValue]: #if chain priorly exists
				for x in range(0,len(self.data[hashedValue])):
					if self.data[hashedValue][x][0] == key:
						self.data[hashedValue][x] = (key, data)
						inserted = True
				if inserted!=True:
					self.data[hashedValue].append((key,data))
				#print('inserted '+key+' at :'+str(nextHashedValue))
		else:
			raise NotStringError("must insert string keys") 

	#add condition for if its not present...
	def getKey(self,key): #not very hashtable-like if i allow indexing by int? 
		if isinstance(key,str):
			hashedValue = myhash(key,self.size)
			Found = False
			Stop = False
			data = None

			if self.data[hashedValue] == None: #have to check this first otherwise, error is thrown if following elif is first.
				return None

			elif len(self.data[hashedValue]) == 1: #if the stored key name at the hashed value matches the key we are searching for, return data
				if self.data[hashedValue][0][0] == key:
					data = self.data[hashedValue][0][1]
				else:
					return None
				#print('retrieving '+key+' at :'+str(hashedValue))				
			else:
				data = None #assume not present, have to search for it.
				for storedkey, value in self.data[hashedValue]:
					if storedkey == key: #if present, set data to value
							data = value
			return data
		else:
			#print("Key you are searching for is neither an int nor a string...")
			raise NotStringError("The key is not a string. Please search for a string hashed location")

	def removeKey(self,key):
		#If chaining is added this has to check through the array and remove the node containing the value we want out.
		i = 0
		if isinstance(key,str):
			hashedValue = myhash(key,self.size)
			if self.data[hashedValue] == None: #trying to remove an empty value in a hashtable just sets it to None again.
				self.data[hashedValue] == None 
			elif len(self.data[hashedValue]) == 1:
				self.data[hashedValue] = None
			else:
				for storedkey, value in self.data[hashedValue]:
					if storedkey == key:
						del self.data[hashedValue][i]
					i+=1 # to know where the key, value pair is
		else:
			#print("Key you are trying to remove is neither an int nor a string...")
			return -1

	def __setitem__(self,key,data):
		self.put(key,data)
	def __getitem__(self,key):
		self.getKey(key)
	def __delitem__(self,key):
		self.removeKey(key)
	def __str__(self):
		return str(self.data)



#further develop my test cases!
class TestHashTable(unittest.TestCase):
	
	def test_empty_hashtable(self):
		test = hashtable(0)
		pt1 = len(test.data)
		actual = pt1
		expected = 0
		self.assertEqual(actual, expected)
	
	def test_not_in_hashtable_key(self):
		test = hashtable(11)
		test.put('cab',1)
		actual = test.getKey('cabz')
		expected = None
		self.assertEqual(actual, expected)
	
	def test_not_in_hashtable_int(self):
		def testing():
			test = hashtable(11)
			test.put('cab',1)
			actual = test.getKey(1)
			expected = None
		self.assertRaises(NotStringError, testing)
   
	def test_in_hashtable(self):
		test = hashtable(11)
		test.put('cab',1)
		actual = test.getKey('cab')
		expected = 1
		self.assertEqual(actual, expected)
	
	def test_in_hashtable_chain(self):
		test = hashtable(11)
		test.put('z',1)
		test.put('g',2)
		test.put('d',3)
		actual = test.getKey('d')
		expected = 3
		
		self.assertEqual(actual, expected)

	def test_overwrite_previous_value(self):
		test = hashtable(11)
		test.put('z',1)
		test.put('g',2)
		test.put('d',3)
		test.put('d',4)
		actual = test.getKey('d')
		expected = 4
		self.assertEqual(actual, expected)

	def test_remove(self):
		test = hashtable(11)
		test.put('z',1)
		test.put('g',2)
		test.put('d',3)
		test.put('d',4)
		test.removeKey('d')
		actual = test.getKey('d')
		expected = None
		self.assertEqual(actual,expected)

	def test_inserting_new_key_when_max_capacity(self):
		test = hashtable(11)
		i = 0
		for char in string.ascii_lowercase:
			if i == 11:
				break
			test.put(char,'1')
			i+=1
		test.put('z',55)
		actual = test.getKey('z')
		expected = 55

		self.assertEqual(actual,expected)

if __name__ == '__main__':
	unittest.main(verbosity=2)
	test2 = hashtable(17)
	test2.put('testing',3)
	print(str(test2))
