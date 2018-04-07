from flask import Blueprint,render_template
from simpledu.models import Course

#如果省略了url_prefix，那么就默认是'/'
front = Blueprint('front',__name__)

@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html',courses=courses)
