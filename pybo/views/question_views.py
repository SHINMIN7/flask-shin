#질문 목록 조회와 질문(코인 판매글) 상세 조회 기능
from datetime import datetime
from flask import Blueprint, render_template, request, url_for, g
from werkzeug.utils import redirect
from .. import db
from pybo.models import Question
from ..forms import QuestionForm
from pybo.views.auth_views import login_required




bp = Blueprint('question',__name__,url_prefix='/question')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    #작성일시 기준 역순으로 정렬
    question_list = Question.query.order_by(Question.create_date.desc()) # 조회 결과를 정렬
    question_list = question_list.paginate(page=page, per_page=10)
    #템플릿 파일을 화면에 그려줌, 전달받은 데이터로 화면 구성
    return render_template('question_list.html', 
                           question_list=question_list)

@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    return render_template('question_detail.html',question=question)


@bp.route('/create/',methods=('GET','POST'))
@login_required
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, 
                            create_date=datetime.now(), user = g.user)
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question_form.html',form=form)
