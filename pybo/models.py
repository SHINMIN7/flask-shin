from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True) #코인 판매 게시물의 고유 번호
    subject = db.Column(db.String(200),nullable = False) #게시물 제목
    content = db.Column(db.Text(),nullable =False) # 게시물 내용
    create_date = db.Column(db.DateTime(),nullable=False) # 게시물 작성일시
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)