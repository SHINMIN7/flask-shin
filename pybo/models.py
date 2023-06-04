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
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'),nullable = False) 
    #유저 데이터의 고유 번호, 어떤 유저 계정에 대한 입금인지 알아야 하므로
    amount = db.Column(db.Integer, nullable = False) # 입금 금액
    timestamp = db.Column(db.DateTime(), nullable = True) # 입금 시간
   
    
    #유저 계정과 연동하기 위해 추가

    
#출금 모델
class Withdraw(db.Model):
    id = db.Column(db.Integer, primary_key=True) #출금 고유번호
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'),nullable = False)
    amount = db.Column(db.Integer, nullable = False) #출금 금액
    timestamp = db.Column(db.DateTime(), nullable = True)  #출금 시간





    #create_date_deposit = db.Column(db.DateTime(),nullable=False) # 입금 시간
    #create_date_withdraw = db.Column(db.DateTime(),nullable=False) # 출금 시간
    #coins = db.Column(db.Integer) # 보유 코인
    
    #def __init__(self, name, balance=0, coins =0):
    #     self.username = name
    #     self.balance = balance
    #     self.coins = coins
    # #추가된 코드
