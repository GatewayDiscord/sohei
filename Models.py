from sohei.main import db

class Users(db.Model):
    username=db.Column(db.String(100), primary_key=True)
    password=db.Column(db.String(100))
    role=db.Column(db.String(100))
    registered_on=db.Column(db.String(100))

    def __init__(self, username, password,registered_on, role):
        self.username=username
        self.password=password
        self.registered_on=registered_on
        self.role=role

    def init_db(self):
        db.create_all()

    if __name__=="__main__":
        init_db()

