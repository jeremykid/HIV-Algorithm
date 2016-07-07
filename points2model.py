from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def main():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')

	f = open("out","r")
	content = f.read().splitlines()
	x = []
	y = []
	z = []
	for i in content:
		point_list = i.split()
		x.append(float(point_list[0]))
		y.append(float(point_list[1]))
		z.append(float(point_list[2]))


	ax.scatter(x, y, z, c='r', marker='o')

	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	plt.show()
main()	