# Github Rest Api

import requests

class Github:
    def __init__(self):
        self.api_url = "https://api.github.com"
        self.token = ""

    def get_User(self, username):
        response = requests.get(self.api_url + '/users/' + username)
        return response.json()

    def get_Repositories(self,username):
        response = requests.get(self.api_url + '/users/' + username)
        user_data =  response.json()
        
        if 'repos_url' in user_data:
            repos_url_object = user_data['repos_url']
            repos_response = requests.get(repos_url_object)
            return repos_response.json()
        else:
            return []

    def create_Repositories(self, name):
        response = requests.post(
            self.api_url + '/user/repos',
            headers={'Authorization': 'token ' + self.token}, 
            json={
                "name": name,
                "description": "This is your first repository",
                "homepage": "https://github.com/muratkazma0",
                "private": False,
                "has_issues": True,
                "has_projects": True,
                "has_wiki": True
            }
        )

        if response.status_code == 201:
            print("Repository created successfully!")
        else:
            print("Failed to create repository. Status code:", response.status_code)
            print("Error message:", response.json())

        return response.json()

github = Github()

while True:
    election = input(
        '1- Find User\n2- Get Repositories\n3- Create Repository\n4- Exit\n Preference : ')

    if election == '4':
        break
    else:
        if election == '1':
            username = input('username : ')
            result = github.get_User(username)
            print(f"name : {result['name']} public repos : {result['public_repos']} follower : {result['followers']} ")

        elif election == '2':
            username = input('username : ')
            result = github.get_Repositories(username)
        
            for repo in result:
                print(repo['name'])

        elif election == '3':
            name = input('Repository name : ')
            result = github.create_Repositories(name)
        else:
            print('Wrong Selection!')
