from exts import db
from flask_sqlalchemy import SQLAlchemy

class EntityBase(object):
    def to_json(self):
        fields = self.__dict__
        if "_sa_instance_state" in fields:
            del fields["_sa_instance_state"]
        return fields

class index(db.Model ,EntityBase) :
    __tablename__ = 'index'
    table_name = db.Column(db.String(255), primary_key = True)
    titles = db.Column(db.String(4096))
    chinese_table_name = db.Column(db.String(255))
    chinese_titles = db.Column(db.String(4096))
    def __repr__(self) -> str:
        return '<JXLB %r>' % self.chinese_table_name