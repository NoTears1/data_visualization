import pygal

from die import Die

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(50000):
    result = die_1.roll()+die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result):
    frequency = results.count(value)
    frequencies.append(frequency)

# 创建条形图，对结果进行可视化
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist._x_title = "Results"
hist._y_title = "Frequency of Result"

hist.add('D6+D10', frequencies) # 将一系列值添加到图表中，传递要给添加的值指定的标签和一个包含值的列表
hist.render_to_file('D6+D10_visual.svg')