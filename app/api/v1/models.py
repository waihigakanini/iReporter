red_flag_list = []

class RedFlagModel():
    """class for redflag model"""
    def __init__(self):
        """"""
        self.db = red_flag_list

    def save(self, data):
        """method for creating and adding an incident"""
        data['id'] = len(self.db) + 1
        self.db.append(data)
    
    def find(self, id):
        """method for finding an incident in a list"""
        for incident in self.db:
            if incident['id'] == id:
                return incident
        return None

    def delete(self, incident):
        """method for deleting an incident in a list"""
        self.db.remove(incident)

    def get_all(self):
        """method for getting all redflags in a list"""
        return self.db

    def edit_comment(self,id):
        pass
          
