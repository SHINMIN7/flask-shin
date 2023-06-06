#질문 목록 조회와 질문(코인 판매글) 상세 조회 기능
from datetime import datetime
from flask import Blueprint, render_template,flash, request, url_for, g,session
from werkzeug.utils import redirect
from .. import db
from pybo.models import User, Deposit, Withdraw
from ..forms import DepositForm,WithdrawForm
from pybo.views.auth_views import login_required





bp = Blueprint('account',__name__,url_prefix='/account')


@bp.route('/', methods=('GET', 'POST'))
def myaccount(): # 이 함수 호출
    return render_template('account.html')



@bp.route('/deposit/',methods=('GET','POST'))
@login_required
def deposit():
    user = User.query.get_or_404(g.user.id)
    form = DepositForm()
    if request.method == 'POST' and form.validate_on_submit():
        deposit = Deposit(amount = form.amount.data, account_id = user)
        db.session.add(deposit)
        db.session.commit()
        g.user.balance += deposit.amount
        db.session.commit()
        flash('You Have Deposited ${}.'.format(deposit.amount),'success')
        return redirect(url_for('account.myacount'))
    return render_template('deposit.html',form=form)




@bp.route('/withdraw/', methods = ('POST','GET'))
@login_required
def withdraw():
    form = WithdrawForm()
    if request.method == 'POST' and form.validate_on_submit():
        withdraw = Withdraw(amount=form.amount.data, account_id = g.user.id)
        if form.amount.data <= User.balance:
            User.balance -= form.amount.data
            db.session.commit(withdraw)
            flash()
            return redirect('account.myacount')
        else:
           flash("출금 실패")
    return render_template('withdraw.html', form=form)




