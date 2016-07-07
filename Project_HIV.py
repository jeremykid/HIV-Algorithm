import math

class Point:
	"the points"
	x = 0
	y = 0
	z = 0
	index = 0
	# exist = 0
	def __init__(self, x, y, z, index = 0):
		self.x = x
		self.y = y
		self.z = z
		self.index = index
		# self.exist = exist

	def editIndex(self, index):
		self.index = index

	# def editExist(self, exist):
	# 	self.exist = exist

	def __repr__(self):
		return str(self.x)+" "+str(self.y)+" "+str(self.z)+" "+str(self.index)

class Quaternion:
	w = 0
	x = 0
	y = 0
	z = 0

	def __init__(self, theta, x, y, z):
		sintheta = math.sin(theta/2)
		self.w = math.cos(theta/2)
		self.x = x*sintheta
		self.y = y*sintheta
		self.z = z*sintheta


def distance(point_x, point_y): 
	x2 = (point_x.x-point_y.x)**2
	y2 = (point_x.y-point_y.y)**2
	z2 = (point_x.z-point_y.z)**2

	return math.sqrt(x2+y2+z2)

def unit(point_z):
	magnitude = math.sqrt(point_z.x**2 + point_z.y**2 + point_z.z**2)
	
	point_z.x = point_z.x/magnitude
	point_z.y = point_z.y/magnitude
	point_z.z = point_z.z/magnitude
	return point_z,magnitude

def rotate120(point_x, point_y):
	'''
	point_x rotate about point_y
	'''
	sin120 =  math.sqrt(3)/2
	cos120 = -0.5
	pointz = Point(point_y.x, point_y.y, point_y.z)
	newpoint,magnitude = unit(pointz)
	
	x = (cos120+newpoint.x**2*(1-cos120)) * point_x.x +\
		(newpoint.x*newpoint.y*(1-cos120) - newpoint.z*sin120) * point_x.y +\
		(newpoint.x*newpoint.z*(1-cos120) + newpoint.y*sin120) * point_x.z

	y = (newpoint.y*newpoint.x*(1-cos120) + newpoint.z*sin120) * point_x.x +\
		(cos120 + newpoint.y**2*(1-cos120)) * point_x.y +\
		(newpoint.y*newpoint.z*(1-cos120) - newpoint.x*sin120) * point_x.z

	z = (newpoint.z*newpoint.x*(1-cos120) - newpoint.y*sin120) * point_x.x +\
		(newpoint.z*newpoint.y*(1-cos120) + newpoint.x*sin120) * point_x.y +\
		(cos120 + newpoint.z**2*(1-cos120))*point_x.z

	result_point = Point(x,y,z)

	return result_point

def rotate240(point_x,point_y):
	'''
	point_x rotate about point_y 240 degree
	'''
	sin240 =  -math.sqrt(3)/2
	cos240 = -0.5
	pointz = Point(point_y.x, point_y.y, point_y.z)
	newpoint,magnitude = unit(pointz)
	
	x = (cos240+newpoint.x**2*(1-cos240)) * point_x.x +\
		(newpoint.x*newpoint.y*(1-cos240) - newpoint.z*sin240) * point_x.y +\
		(newpoint.x*newpoint.z*(1-cos240) + newpoint.y*sin240) * point_x.z

	y = (newpoint.y*newpoint.x*(1-cos240) + newpoint.z*sin240) * point_x.x +\
		(cos240 + newpoint.y**2*(1-cos240)) * point_x.y +\
		(newpoint.y*newpoint.z*(1-cos240) - newpoint.x*sin240) * point_x.z

	z = (newpoint.z*newpoint.x*(1-cos240) - newpoint.y*sin240) * point_x.x +\
		(newpoint.z*newpoint.y*(1-cos240) + newpoint.x*sin240) * point_x.y +\
		(cos240 + newpoint.z**2*(1-cos240))*point_x.z

	result_point = Point(x,y,z)
	return result_point

def readFromCsv():

	return 0

def general_input():
	with open("in") as f:
		content = f.read().splitlines()
		K_index = int(content[0])
		K_keepers = []
		for i in range(K_index):
			a = content[i+1].split()
			new_point = Point(float(a[0]),float(a[1]),float(a[2]),i+1)
			K_keepers.append(new_point)
		P_index = int(content[K_index+1])
		P_pivots = []
		for i in range(P_index):
			a = content[i+K_index].split()
			new_point = Point(float(a[0]),float(a[1]),float(a[2]),i+1)
			P_pivots.append(new_point)


	return K_keepers,K_index,P_index,P_pivots

def general_write():
	with open("out","w") as w:
		w.write(str(123)+"\n")
		w.write("str"+ "\n")

def get_root_index(index):
	if index == 2:
		return 1
	elif index%2:
		return (index-1)/2
	else:
		return (index-2)/2

def check_distance(point_x,point_y):
	distance = math.sqrt((point_x.x-point_y.x)**2+(point_x.y-point_y.y)**2+(point_x.z-point_y.z)**2)
	# print (distance)
	if distance >= 52:
		return True
	else:
		return False

def check_everydistance(point_x,K_keepers):
	for i in K_keepers:
		if i and not check_distance(i,point_x):
			return False
	return True



def main():
	K_keepers, K_index,P_index,P_pivots = general_input()

	# point_x = Point(0,0,632.1911456,1)
	# point_y = Point(52.03280151,0,630.0462143,2)
	# print (point_x)
	# listA = [point_x,point_y]

	# print K_keepers, K_index,P_index,P_pivots 
	w = open("out","w")

	K_count = K_index
	K_index += 1
	P_count = P_index
	while (P_count != K_count):
		father = get_root_index(K_index)
		grandfather = get_root_index(father)
		if K_keepers[father-1]:
			new_point = rotate120(K_keepers[grandfather-1],K_keepers[father-1])
			new_point.editIndex(K_index)
			if check_everydistance(new_point,K_keepers):
				K_keepers.append(new_point)
				K_count += 1
				a = new_point
				w.write(str(a))
				print (a)
				w.write("\n")
			else:
				K_keepers.append(0)
			K_index += 1
			new_point = rotate240(K_keepers[grandfather-1],K_keepers[father-1])
			new_point.editIndex(K_index)
			if check_everydistance(new_point,K_keepers):
				K_keepers.append(new_point)
				K_count += 1
				a = new_point
				w.write(str(a))
				print (a)
				w.write("\n")
			else:
				K_keepers.append(0)
			K_index += 1

		else:
			K_keepers.append(0)
			K_keepers.append(0)
			K_index += 2

		if K_keepers[father-1]:
			P_count += 1
		P_index += 1
		P_pivots.append(K_keepers[father-1])

	w.write(P_count,K_count)
	# rotate120(point_x,point_y)
	# rotate240(point_x,point_y)




	return 0
main()
