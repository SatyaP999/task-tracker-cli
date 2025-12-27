from datetime import datetime

class Task:
    def __init__(self, id, description):
        self.id = id
        self.description = description
        self.status = "todo"
        self.createdAt = datetime.now().isoformat()
        self.updatedAt = self.createdAt
        
    
    def __str__(self):
        return f"""
            --> Task ID: {self.id} \n
            --> Task Description: {self.description} \n
            --> Task status: {self.status} \n
            --> Task created at : {self.createdAt} \n
            --> Task updated at : {self.updatedAt} \n
        """
    
    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt
        }
    