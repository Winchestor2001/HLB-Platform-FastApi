from piccolo.columns import Varchar, ForeignKey, Integer, Boolean, Float, Text, M2M, LazyTableReference
from piccolo.table import Table
from src.auth.tables import BaseMixin


class Course(BaseMixin, Table):
    name = Varchar(length=255)
    poster_image = Varchar(length=255)
    paid = Boolean(default=False)
    price = Float(null=True)


class Lesson(BaseMixin, Table):
    course = ForeignKey(Course)
    number = Integer(default=1)
    name = Varchar(length=255)
    paid = Boolean(default=False)
    price = Float(null=True)
    quiz = M2M(LazyTableReference("LessonQuiz", module_path=__name__))


class Article(BaseMixin, Table):
    lesson = Varchar(length=255)
    name = Varchar(length=255)
    file = Varchar(length=255)
    context = Text(null=True)
    read_time = Integer(default=0)
    quiz = M2M(LazyTableReference("ArticleQuiz", module_path=__name__))


class Quiz(BaseMixin, Table):
    question = Varchar(length=255)
    answer = Varchar(length=255)
    mark_1 = Varchar(length=200)
    mark_2 = Varchar(length=200)
    mark_3 = Varchar(length=200)
    mark_4 = Varchar(length=200)
    score = Integer()


class ArticleQuiz(BaseMixin, Table):
    article = ForeignKey(Article)
    quiz = ForeignKey(Quiz)


class LessonQuiz(BaseMixin, Table):
    lesson = ForeignKey(Lesson)
    quiz = ForeignKey(Quiz)
