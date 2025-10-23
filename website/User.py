from flask_login import UserMixin

class User(UserMixin):
        def __init__(self, doc):
            self.doc = doc or {}
            self.id = str(self.doc.get("_id"))

        @property 
        def is_active(self):
            return bool(self.doc.get("is_active", True))
        
        @property
        def username(self):
             return str(self.doc.get("first_name"))