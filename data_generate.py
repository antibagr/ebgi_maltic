import os

import pickle
import random

# return data as array
def getdata(reload_data=False):
	BASE_DIR = os.path.abspath(os.path.dirname(__file__))

	filename = 'data.txt'

	filepath = os.path.join(BASE_DIR,filename)

	def makearray():
		return [ random.randint(0,1000) for x in range(1,10) ]

	def writedata():
		with open(filepath,'wb') as f:
				arr = makearray()
				pickle.dump(arr,f)

	def fileisbroken():
		try:
			with open(filepath,'rb') as f:
				pickle.load(f)
		except pickle.UnpicklingError:
			return True

	# do i need to generate new data?
	def togenerate():
		if os.path.exists(filepath):
			if os.path.getsize(filepath) != 0:
				if not fileisbroken():
					if not reload_data:
						return False

		return True

	if togenerate():
		writedata()

	with open(filepath,'rb') as f:
		return pickle.load(f)