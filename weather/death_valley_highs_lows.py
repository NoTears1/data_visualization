import csv
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather/death_valley_2021_simple.csv')
lines = path.read_text().splitlines() #获取一个包含文件中各行的列表

reader = csv.reader(lines) # reader()解析文件各行并将每项数据作为一个元素存储在列表中
header_row = next(reader) # next()从文件开头开始返回文件的下一行，其中包括文件头

#print(header_row)
    
# # 打印文件头及其位置
# for index, column_header in enumerate(header_row): # enumerate()获取每个元素的索引及其值
#   print(index, column_header)

# 提取并读取数据
dates, highs, lows= [], [], []
# reader对象从刚才中断的地方继续向下读取文件，每次返回当前位置的下一行，
# 由于已经读取了文件头行，这个循环从第二行开始
for row in reader: 
  current_date = datetime.strptime(row[2], '%Y-%m-%d')
  try: # 防止出现温度的缺失值
    # 文件中数据以字符串格式存储，因此需要转为int格式方便使用
    high = int(row[3])
    low = int(row[4])
  except ValueError:
    print(f"Missing data for {current_date}")
  else:
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
# print(highs)

# 根据最高温度绘图
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5)
ax.plot(dates, lows, color = 'blue', alpha = 0.5) # alpha指定颜色的透明度
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1) #根据传入的坐标在区域内填充指定的颜色
# 设置绘图的格式
ax.set_title("Daily High and Low Temperatures, 2021\nDeath Valley, CA", fontsize = 20)
ax.set_xlabel('', fontsize = 16)
ax.set_ylabel("Temperature (F)", fontsize = 16)
fig.autofmt_xdate() # 绘制倾斜的日期标签
ax.tick_params(labelsize = 16)

plt.show()