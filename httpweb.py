import requests
import json

class HttpService:
    def __init__(self, baseUrl):
        self.baseUrl = baseUrl

    def getUsers(self, userId = None):
        if userId is not None:
            r = requests.get(self.baseUrl + 'users/' + str(userId)).json()
            return r
        else:
            return requests.get(self.baseUrl + 'users').json()

    def getPosts(self):
        return requests.get(self.baseUrl + 'posts').json()

    def getPosts(self, postId):
        return requests.get(self.baseUrl + 'posts/' + postId).json()


baseUrl = 'https://jsonplaceholder.typicode.com/'
print "Sending request..."
AllUsers = HttpService(baseUrl).getUsers()
FirstUser = HttpService(baseUrl).getUsers(1)


#result = requests.get(baseUrl + 'users').json()

print AllUsers
print "\n\n\n"
print FirstUser

