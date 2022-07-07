from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Book:
    title = db.Column(db.String(100))
    url = db.Column(db.String(100))
    abstract = db.Column(db.String(500))
    body_text = db.Column(db.String(1000))
    body_html = db.Column(db.String(1000))
    id = db.Column(db.Integer, primary_key=True)

    def save(self):
        db.session.add(self)
        db.session.commit()


class BookDe(db.Model, Book):
    __tablename__ = 'de'


class BookEn(db.Model, Book):
    __tablename__ = 'en'


class BookRu(db.Model, Book):
    __tablename__ = 'ru'
