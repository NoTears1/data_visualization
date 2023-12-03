import matplotlib.pyplot as plt
'''绘制散点图'''
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values] # x**2 为x的平方
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s = 40) 
    # edgecolors设置数据点的轮廓，默认为蓝色点和黑色轮廓
    # c表示数据点颜色，可以用颜色的英语单词赋值，也可以用RGB元组赋值，即c=(0, 0, 0.8)，范围为0~1，值越大颜色越浅
    # 在颜色映射中，c也可以设置为一个列表，根据值的大小确定不同点颜色的深浅
    # cmap表示设置颜色映射的颜色

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis="both", which='major', labelsize = 14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0 ,1100000])

# 自动保存图表
plt.savefig('square_plot.png', bbox_inches = 'tight')
    # bbox_inches指定将多余的空白裁剪