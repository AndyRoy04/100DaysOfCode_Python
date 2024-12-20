# Diving into creating classes and objects
class User():
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def get_followers(self, user):
        user.followers += 1
        self.following += 1

user1 = User('213', "Anderson")
user2 = User('214', "Carla")

user1.get_followers(user2)
print(user1.user_name)  
print(user1.followers)
print(user2.followers)
print(user2.user_name)  
print(user1.following)
print(user2.following)
