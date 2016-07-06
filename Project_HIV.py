import math

class Point:
	"the points"
	x = 0
	y = 0
	z = 0
	index = 0
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def editIndex(self, index):
		self.index = index
		
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
	print(point_z.x,point_z.y,point_z.z)
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

	print (z)

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

	print (x)

def readFromCsv():

	return 0

def main():
	point_x = Point(0,0,632.1911456)
	point_y = Point(52.03280151,0,630.0462143)



	rotate120(point_y,point_x)
	rotate240(point_y,point_x)

	P_index = 3
	K_index = 0

	return 0
main()
