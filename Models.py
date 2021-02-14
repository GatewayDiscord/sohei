from sohei.main import db

class Users(db.Model):
    __tablename__="users"

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


class challenges(db.Model):
    __tablename__="challenges"

    challengeid=db.Column(db.String(100), primary_key=True)
    title=db.Column(db.String(100))
    body=db.Column(db.String(140))
    tag=db.Column(db.String(100))
    category=db.Column(db.String(100))
    ctfid=db.Column(db.String(100),
            db.ForeignKey("ctfs.ctfid", ondelete="CASCADE"))

    def __init__(self, id, title, body, tag, category, eventname):
        self.id=id
        self.title=title
        self.body=body
        self.tag=tag
        self.category=category
        self.ctfid=ctfid

    def init_db(self):
        db.create_all()

class CTFs(db.Model):
    __tablename__="ctfs"

    ctfid=db.Column(db.String(100), primary_key=True)
    ctftitle=db.Column(db.String(100))
    link=db.Column(db.String(100))
    status=db.Column(db.String(100)) #ongoing, done or upcoming
    date=db.Column(db.String(100))

    def __init__(self, ctfid, ctftitle, link, status, date):
        self.ctfid=ctfid
        self.ctftitle=ctftitle
        self.link=link
        self.status=status
        self.date=date


class files(db.Model):

    __tablename__="files"

    fileid=db.Column(db.String(100), primary_key=True)
    challengeid=db.Column(db.String(100), 
            db.ForeignKey("challenges.challengeid", ondelete="CASCADE"))
    filehash=db.Column(db.String(100))

    def __init__(self, fileid, challengeid, filehash):
        self.fileid=fileid
        self.challengeid=challengeid
        self.filehash=filehash

if __name__=="__main__":
    init_db()
