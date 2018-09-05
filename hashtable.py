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
def rehash(prevval, size):
	#print('rehashing'+str(prevval))
	prevval += 3
	return prevval%size

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
		self.keys = [None]*size #for optimization can just add keys to data array.  
		self.spaceAvail = size




	def put(self,key,data):
		insertionAttemps = 1
		hashedValue = myhash(key,self.size)

		#check space available.. since linear probing this will work. if collisions can stack, i.e chaining this will not.
		#if self.spaceAvail > 0 :
		#	self.spaceAvail -= 1
		#elif key in self.keys: #since self.keys is an array, the in operator is O(n), but this operation only occurs in worst case of full hashtable + overwrite insertion. 
			#print('hashtable is filled but can overwrite..')
		#	self.spaceAvail+=0 #just doing nothing
		#else:
			#statement = "no more space to insert a new key"
			#print(statement)
		#	return -1 #why cant i return the string here?

		if isinstance(key,str):
			#insert if empty position.
			if self.data[hashedValue] == None:
				print("inserting :"+key+"at hashed value :"+str(hashedValue))
				self.data[hashedValue] = data
				self.keys[hashedValue] = key
				#print('inserted '+key+' at :'+str(hashedValue))
				self.spaceAvail -= 1

			elif self.keys[hashedValue] == key: #if key previously exists in table and is the same as the key we are trying to place, replace the data
				self.data[hashedValue] = data
				self.spaceAvail -= 1
				#print('inserted '+key+' at :'+str(hashedValue))
			else:
				#print("can't insert "+key+" at hashed index "  +str(hashedValue) +" rehashing...")
				insertionAttemps +=1
				nextHashedValue = rehash(hashedValue, self.size)
				#while key slots already have a value, and that value is not the key we're trying to hash
				while(self.keys[nextHashedValue]!=None and self.keys[nextHashedValue]!=key): 
					nextHashedValue = rehash(nextHashedValue, self.size)
					insertionAttemps+=1
					if insertionAttemps>self.size:
						print("this got triggered")
						raise NoSpaceError #("The hashtable is full and can't accept new key-value pairs.")
				print('\nI am here')
				print('the rehashed value is ' +str(nextHashedValue))
				print('the key to insert is : '+key)
				print('the data to insert is : '+str(data))
				self.keys[nextHashedValue] = key
				self.data[nextHashedValue] = data
				print('checking whats in the hashtable :'+self.keys[nextHashedValue])
				print('checking whats in the hashtable values :' +self.data[nextHashedValue])
				self.spaceAvail -= 1
				#print('inserted '+key+' at :'+str(nextHashedValue))
		else:
			print("Error, key must be a string")
			return -1 

	#add condition for if its not present...
	def getKey(self,key): #not very hashtable-like if i allow indexing by int? 
		if isinstance(key,int):
			if self.keys[key]:
				return self.data[key]
			else:
				#print("the specified integer key holds nothing.")
				return None

		elif isinstance(key,str):
			hashedValue = myhash(key,self.size)
			Found = False
			Stop = False
			startHash = hashedValue
			data = None

			if self.keys[hashedValue] == key: #if the stored key name at the hashed value matches the key we are searching for, return data
				data = self.data[hashedValue]
				#print('retrieving '+key+' at :'+str(hashedValue))
			elif self.keys[hashedValue] == None:
				#print("the string key you are searching for is not present in the hashtable")
				return None
			else:
				nextHashedValue = rehash(hashedValue, self.size)
				#print("the key at the hashed value is not what we're looking for...") #initially testing if it finds the collision or not.
				#should improve this to just check down the chain... but for now rehash until it finds they key we need.
				#also at some point the hashtable might be full. need to check if we cant insert anymore and exit.
				while(self.keys[nextHashedValue]!=key and not Found and not Stop): 
					if self.keys[nextHashedValue] == key:
						return self.data[nextHashedValue]
					else:
						nextHashedValue = rehash(nextHashedValue, self.size)
						if nextHashedValue == startHash:
							Stop = True
							return None
			return data
		else:
			#print("Key you are searching for is neither an int nor a string...")
			raise NotStringError("The key is not a string. Please search for a string or use an int representing hashed location")

	def removeKey(self,key):
		#If chaining is added this has to check through the linked list and remove the node containing the value we want out.
		self.spaceAvail+=1 #valid without linear probing.
		if isinstance(key,int):
			self.data[key] = None
			self.keys[key] = None

		elif isinstance(key,str):
			hashedValue = myhash(key,self.size)
			if self.keys[hashedValue] == key: #if the stored key name at the hashed value matches the key we are searching for
				self.keys[hashedValue] == None
				self.data[hashedValue] == None
			else:
				nextHashedValue = rehash(hashedValue, self.size)
				while(self.keys[nextHashedValue]!=key): 
					nextHashedValue = rehash(nextHashedValue, self.size)
				self.keys[nextHashedValue] == None
				self.data[nextHashedValue] == None
		else:
			#print("Key you are trying to remove is neither an int nor a string...")
			return -1

	def __setitem__(self,key,data):
		self.put(key,data)
	def __getitem__(self,key):
		self.getKey(key)
	def __delitem__(self,key):
		self.removeKey(key)



#further develop my test cases!
class TestHashTable(unittest.TestCase):
	"""
	def test_empty_hashtable(self):
		test = hashtable(0)
		pt1 = len(test.data)
		pt2 = len(test.keys)
		actual = pt1+pt2
		expected = 0
		self.assertEqual(actual, expected)
	
	def test_not_in_hashtable_int(self):
		test = hashtable(11)
		test.put('cab',1)
		actual = test.getKey(0)
		expected = None
		self.assertEqual(actual, expected)

	def test_not_in_hashtable_key(self):
		test = hashtable(11)
		test.put('cab',1)
		actual = test.getKey('cabz')
		expected = None
		self.assertEqual(actual, expected)
    
	def test_in_hashtable(self):
		test = hashtable(11)
		test.put('cab',1)
		actual = test.getKey('cab')
		expected = 1
		self.assertEqual(actual, expected)
    
	def test_overwrite_previous_value(self):
		test = hashtable(11)
		i = 0
		for char in string.ascii_lowercase:
			if i == 11:
				break
			test.put(char,'1')
			i+=1
		before = test.getKey(1)	
		test.put('d',55)
		after = test.getKey('d')
		self.assertEqual(after,55)

	def test_inserting_new_key_when_max_capacity(self):
		def testing():
			test = hashtable(11)
			i = 0
			for char in string.ascii_lowercase:
				if i == 11:
					break
				test.put(char,'1')
				i+=1
			test.put('z',55)
		self.assertRaises(NoSpaceError,testing)

	def test_find_hashed_value_c(self):
		#check that hashing resets to 0 once it exceed maximum space
		test = hashtable(11)
		i = 0
		for char in string.ascii_lowercase:
			if i == 3:
				break
			test.put(char,char)
			i+=1
		actual = test.getKey(0)	
		expected = 'c'
		self.assertEqual(actual,expected)

	def test_find_rehashed_value_z(self):
		#check that hashing inserts at location 4 since location 1 is filled already
		test = hashtable(11)
		i = 0
		for char in string.ascii_lowercase:
			if i == 4:
				break
			test.put(char,char)
			i+=1
		test.put('z','z')
		actual = test.getKey(4)	
		expected = 'z'
		self.assertEqual(actual,expected)
	"""
	def test_find_rehashed_3times_d(self):
		#check that hashing inserts at location 4 since location 1 is filled already"""
		test = hashtable(11)
		test.put('z','z') #goes to location 1
		test.put('g','g') #goes to location 4 
		test.put('j','j') #goes to location 7
		test.put('d','d') #should go to location 10 since 1 is filled.
		actual = test.getKey('d')
		expected = 'd'
		print(test.getKey('z'))
		print(test.getKey('g'))
		print(test.getKey('j'))
		print(test.getKey('d'))

		self.assertEqual(actual,expected)
	
	#def test_get_key_not_string(self):
	#	def testingString():
	#		test = hashtable(11)
	#		test.put('z',55)
	#		test.getKey(1.0)
	#	self.assertRaises(NotStringError,testingString)
	
	#def test_remove_key(self):
	#	test = hashtable(11)
	#	test.put('z','z')
	#	test.removeKey('z')
	#	self.assertEqual(test.spaceAvail,11)		

if __name__ == '__main__':
    unittest.main(verbosity=2)



