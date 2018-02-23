from config import db
def init_db():
    from models.mysql.activity import Activity

    db.create_all()