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
prompt = raw_input("Enter 1 to Retreive all User. 2 to get specific User => ")

if prompt == '1':
    AllUsers = HttpService(baseUrl).getUsers()
    print len(AllUsers), "Users found"
    for User in AllUsers:
        print User["id"], User["name"], User["phone"]
elif prompt == '2':
    Uid = raw_input("Enter UserId. Range is between 1 - 10 => ")
    User = HttpService(baseUrl).getUsers(Uid)
    print User["id"], User["name"], User["phone"]
else:
    print "Invalid Input"
