Users_list = []

class UsersModel():
    """class for user models"""
    def __init__(self):
        self.db = Users_list

    def save(self, data):
        """method for posting users"""
        data['id'] = len(self.db) + 1

        self.db.append(data)
    
    def find(self, id):
        """method for finding users"""
        for user in self.db:
            if user['id'] == id:
                return user
        return None

    def delete(self, user):
        """method for deleting user"""
        self.db.remove(user)

    def get_all(self):
        """method for getting all users"""
        return self.db

    