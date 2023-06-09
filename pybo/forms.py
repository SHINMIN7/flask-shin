from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField,  IntegerField, SubmitField
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


#입금가능한 폼 작성
class DepositForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired('입금 금액을 입력해 주세요'),NumberRange(min=1)])
    #submit = SubmitField('Deposit')

#출금가능한 폼 작성
class WithdrawForm(FlaskForm):
    amount = IntegerField('Amount', validators=[DataRequired('출금 금액을 입력해 주세요'),NumberRange(min=1)])

    
       