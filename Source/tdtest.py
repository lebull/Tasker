from pytodoist import todoist

user = todoist.login_with_api_token('b646e8b461ef6be694d697ccba93da90674f4fcf')
print(user.email)