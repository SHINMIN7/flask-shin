from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField,  FloatField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, NumberRange# ValidationError



class QuestionForm(FlaskForm):
    subject = StringField('제목', validators=[DataRequired('제목을 입력해 주세요')])
    content = TextAreaField('내용', validators=[DataRequired('내용을 입력해 주세요')])
    
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    
 
class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


#입출금 기능
class DepositForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired(),NumberRange(min=0.01)])
    submit = SubmitField('Deposit')

class WithdrawForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired(),NumberRange(min=0.01)])
    submit = SubmitField("Withdraw")
    
    # def __init__(self, user, *args, **kwargs):
    #         self.user = user
    #         super().__init__(*args, **kwargs)
    # def vaildate_amount(self,amount):
    #     if self.user.account.balance < amount.data:
    #         raise ValidationError('계좌 잔액보다 더 많은 돈을 출금할 수 없습니다.')        