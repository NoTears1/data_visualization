import csv

filename = 'sitka_weather_2021.csv'
with open(filename) as f:
    reader = csv.reader(f) # reader处理文件中以逗号分隔的第一行数据，并将每项数据作为一个元素存储在列表中
    header_row = next(reader) # 返回文件的下一行
    
    # 打印文件头及其位置
  #  for index, column_header in enumerate(header_row): # enumerate()获取每个元素的索引及其值
  #      print(index, column_header)

    # 提取并读取数据
    highs = []
    for row in reader:
        highs.append(row[1])

    print(highs)
