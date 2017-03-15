import json , math

#JSON file is assumed to be a list of dictionaries each describing 1 friend

	#JSON Format example:
	#[{"user - id":12 , "name":"asket" , "x_coordinate":84.2232 , "y_coordinate":77.23432}
	# {"user_id":13 , "name":"shubham" , "x_coordinate":86.435} , "y_coordinate":77.4432}
	# ..........
	#]


class inviteFriends:
	x_coordinate = 12.9611159
	y_coordinate = 77.6362214		#static variables
	MAX_DIST = 100
	radius_earth = 6371

	def decode_JSON(self):
		try:
			json_data = open(self.filename , "rb").read()
			self.json_object = json.loads(json_data)

		except IOError:
			print("File does not exist")
			exit()

	def __init__(self , filename = "sample.json"):
		self.filename = filename
		self.json_object = []
		self.invited_friends = []
		try:
			if self.filename[len(self.filename) - 4:len(self.filename)]! = 'json':
				raise Exception
		except:
			print("Not a json file!")
			exit()
		self.decode_JSON()
	
	
	def calculate_dist(self , _x_coordinate , _y_coordinate):		#calculated according to the formula
		del_x = math.fabs(self.x_coordinate - _x_coordinate)
		del_y = math.fabs(self.y_coordinate -  _y_coordinate)
		del_x = (del_x * math.pi) / 360
		del_y = (del_y * math.pi) / 360
		sin_del_x = math.pow(math.sin(del_x) , 2)
		sin_del_y = math.pow(math.sin(del_y) , 2)
		cos_x1 = math.cos((self.x_coordinate * math.pi) / 180)
		cos_x2 = math.cos((_x_coordinate * math.pi) / 180)
		del_sigma = math.asin(math.pow(sin_del_x + (sin_del_y * cos_x1 * cos_x2) , .5))
		return self.radius_earth * del_sigma




	def inviteFriends(self):
		for friend in self.json_object:
			if self.calculate_dist(friend["x_coordinate"] , friend["y_coordinate"]) < self.MAX_DIST:
				self.invited_friends.append((friend["user - id"] , friend["name"]))

		self.invited_friends.sort()

		return self.invited_friends

if __name__  =  =  '__main__':
		
	filename = raw_input("Enter json file ")
	obj = inviteFriends(filename)
	mylist = obj.inviteFriends()
	if len(mylist) =  = 0:
		print("No friends nearby ")
	else:
		print(mylist)

		
