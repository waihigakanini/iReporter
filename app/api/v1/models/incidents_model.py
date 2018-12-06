import datetime
red_flag_list = []
 
class RedFlagsModel():
    def __init__(self):
        self.db = red_flag_list
        
    def get_all(self):
        """method for getting all redflags in a list"""
        if not self.db:
            return "none"
        return self.db
    def save(self, data):
        """method for creating and adding an incident"""
        self.db.append(data)
        return data
    
    def find(self, id):
        """method for finding an incident in a list"""
        for incident in self.db:
            if incident['id'] == id:
                return incident
        return None

    def delete(self, incident):
        """method for deleting an incident in a list"""
        self.db.remove(incident)
        
    def generate_id(self, id):
        """docstring for the generation of incident ids"""
        pass






          
