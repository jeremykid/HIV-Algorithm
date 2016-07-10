
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
def main():

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    with open("lines") as f:
        content = f.read().splitlines()
        count = 0
        for i in content:
            line_list = i.split(' ')
            count += 1
            ax.plot([float(line_list[0]), float(line_list[4])], [float(line_list[1]),float(line_list[5])],zs=[float(line_list[2]),float(line_list[6])], c= plt.cm.jet(1. * count / 1067) )

    plt.show()
main()