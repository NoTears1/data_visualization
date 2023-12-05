import matplotlib.pyplot as plt

from random_walk import RandomWalk

def rw_visual():
    # 创建一个RandomWalk实例，并将其包含的点都计算出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    # figure()指定图表的宽度、高度、分辨率和背景色，单位为英寸
    plt.figure(figsize=(10, 6))

    # 使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # 书上原为axes()，但结果是图像消失，坐标轴没有消失且错乱
    # 原因在于plt.axes()实际上是创建了一个新的图像覆盖了原来的图像
    plt.gca().get_xaxis().set_visible(False)
    plt.gca().get_yaxis().set_visible(False)
    
    plt.show()

'''模拟多次随机漫步，只要程序处于活动状态，就不断地模拟随机漫步'''
while True:
    rw_visual()
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break