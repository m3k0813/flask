from pybo import db

#질문 모델 id/제목/내용/작성일자
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)        #고유 번호
    subject = db.Column(db.String(200), nullable=False)        #column 클래스는 데이터타입이나 속성을 지정
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

#답변 모델
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))      #질문 모델과 연결
    question = db.relationship('Question', backref=db.backref('answer_set'))                   #relationship으로 속성 추가
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)