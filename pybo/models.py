from pybo import db
from datetime import datetime

class Question(db.Model):
    id = db.Column(db.Integer,primary_key=True) #코인 판매 게시물의 고유 번호
    subject = db.Column(db.String(200),nullable = False) #게시물 제목
    content = db.Column(db.Text(),nullable =False) # 게시물 내용
    create_date = db.Column(db.DateTime(),nullable=False) # 게시물 작성일시
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable = False)
    password = db.Column(db.String(200), nullable=False)
    balance = db.Column(db.Integer, default=0) #잔액
    

    
    
 #입금 모델   
class Deposit(db.Model):
    id = db.Column(db.Integer, primary_key=True) #입금 데이터의 고유번호
    account_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE')) # 계정 모델과 연동
    #입금 모델은 어느 계정에 대한 입금인지 알아야 하므로 계정 모델과 연결된 속성 포함해야 함
    #account = db.relationship('User',backref = db.backref('deposit_set', )) 
    amount = db.Column(db.Integer, nullable = False) # 입금 금액
    #timestamp = db.Column(db.DateTime(), nullable = True) # 입금 시간
    #유저 데이터의 고유 번호, 어떤 유저 계정에 대한 입금인지 알아야 하므로
    #유저 모델을 통해 테이블이 생성되면 테이블명은 user가 된다.
    #deposit 모델의 user_id는 user 테이블의 id 컬럼과 연결된다.
    



    
#출금 모델
class Withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True) #출금 고유번호
    account_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'))
    amount = db.Column(db.Integer, nullable = False) #출금 금액
    #timestamp = db.Column(db.DateTime(), nullable = True)  #출금 시간



