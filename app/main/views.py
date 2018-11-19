from flask_login import login_required

@main.route('/pitch',methods = ['GET','POST'])
@login_required
def new_review(id):