from flask import Blueprint,render_template
from simpledu.models import Course

#省略了url_prefix,那么默认就是'/'
front = Blueprint('front',__name__)
@front.route('/')
def index():
    courses=Course.query.all()
    return render_template('index.html',courses=courses)

@front.route('/login')
def login():
    return render_template('login.html')

@front.route('/register')
def register():
    return render_template('register.html')
