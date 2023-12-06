from pathlib import Path
import json
import plotly.express as px

# 读取数据并转换为Python对象
path = Path('earthquake/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='UTF-8') # 文件改为30天时，不知道问什么用gbk解码，需要指定解码方式
all_eq_data = json.loads(contents) # 转换成字典

# 创建一个更可读的数据文件
path = Path('earthquake/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4) # indent指定嵌套数据的缩进格数
# path.write_text(readable_contents)

# 统计数据集中的地震次数
all_eq_dicts = all_eq_data['features']

# 提取每次地震的规模、地点
mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

# 绘制世界地图
title = 'Global Earthquakes'
fig = px.scatter_geo(lat = lats, lon = lons, size=mags, title = title, 
                     color=mags, color_continuous_scale='Viridis', 
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     hover_name=eq_titles)

fig.show()

