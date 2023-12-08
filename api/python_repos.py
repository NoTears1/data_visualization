import requests

# 发起一个API call并且检查response
url = "https://api.github.com/search/repositories"
url += "?q=language:python+sort:stars+stars:>10000"

headers = {"Accept":"application/vnd.github.v3+json"} # v3表示GitHub的api目前是第三版
r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}") 
# 显示返回的状态，200表示成功；
# print加入f之后，可以直接在字符串中填入需要替换的字符

# 将response对象转换为字典
response_dict = r.json()

# print(f"Total repositories:{response_dict['total_count']}")
# print(f"Complete results:{not response_dict['incomplete_results']}")

# 展示仓库信息
repo_dicts = response_dict['items']
# print(f"Repositories returned:{len(repo_dicts)}")

# 检查第一个仓库
repo_dict = repo_dicts[0]
# print(f"\nKeys:{len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

# 打印仓库的详细信息
print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print(f"Name:{repo_dict['name']}")
    print(f"Owner:{repo_dict['owner']['login']}")
    print(f"Stars:{repo_dict['stargazers_count']}")
    print(f"Repository:{repo_dict['html_url']}")
    print(f"Description:{repo_dict['description']}")

