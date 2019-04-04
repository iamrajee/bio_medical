import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
xs = []
ys = []

def animate(i):
    # graph_data = open('example.txt','r').read()
    # lines = graph_data.split('\n')
    
    # # count = 0
    # for line in lines:
    #     if len(line) > 1:
    # # while count<100:
    #         x, y = line.split(',')
    #         # x,y = count,5
    #         # count = count+1
    #         xs.append(float(x))
    #         ys.append(float(y))
    #         # plt.show()
    ax1.clear()
    ax1.plot(xs, ys)
    

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()