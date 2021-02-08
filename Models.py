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


class CTFs(db.Model):
    id=db.Column(db.String(100), primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.String(140))
    tag=db.Column(db.String(100))
    category=db.Column(db.String(100))

    def __init__(self, id, title, body, tag, category):
        self.id=id
        self.title=title
        self.body=body
        self.tag=tag
        self.category=category

    def init_db(self):
        db.create_all()


if __name__=="__main__":
    init_db()
