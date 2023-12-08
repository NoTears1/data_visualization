import requests
import plotly.express as px

# 发起一个API call并且检查response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"} # v3表示GitHub的api目前是第三版
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}") 
# 显示返回的状态，200表示成功；
# print加入f之后，可以直接在字符串中填入需要替换的字符

# 将response对象转换为字典
response_dict = r.json()
# print(f"Total repositories:{response_dict['total_count']}")
print(f"Complete results:{not response_dict['incomplete_results']}")

# 处理仓库的信息
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    # 创建hover_text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f'{owner}<br />{description}'
    hover_texts.append(hover_text)

# 制作可视化
title = "Most-Starred Python Projects on GitHub"
labels = {'x':'Repository', 'y':'Stars'}
fig = px.bar(x=repo_links, y=stars, labels=labels, title=title, hover_name=hover_texts)

fig.update_layout(title_font_size = 28, xaxis_title_font_size=20, yaxis_title_font_size=20) # 修饰指定的图表中元素
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)
fig.show()
