from flask_login import login_required,current_user
from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos


# @main.route('/pitch/review/new/<int:id>', methods = ['GET','POST'])
# def new_review(id):
#     form = UpdateProfile()
#     pitch = get_pitch(id)

#     if form.validate_on_submit():
#         title = form.title.data
#         review = form.review.data
#         new_review = Review(pitch.id,title,pitch.poster,review)
#         new_review.save_review()
#         return redirect(url_for('pitch',id = pitch.id ))

#     title = f'{pitch.title} review'
#     return render_template('new_review.html',title = title, review_form=form, pitch=pitch) 
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    
    return render_template("profile/profile.html",user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    entertainment = Pitch.query.filter_by(category = 'entertainment')
    business = Pitch.query.filter_by(category = 'business')
    religion = Pitch.query.filter_by(category = 'religion')
    comedy = Pitch.query.filter_by(category = 'comedy')

    comments = Comment.query.all()
    return render_template('index.html',  comments = comments,entertainment = entertainment,business = business, religion = religion, comedy = comedy)

@main.route('/add/pitch',methods = ['GET','POST'])
def add_pitch():
    form = PitchForm()

    if form.validate_on_submit():
        title = form.Title.data
        pitch = form.pitch.data
        category = form.category.data
        
        new_pitch = Pitch(title = title, pitch = pitch, user = current_user, category = category)
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))

    return render_template('add_pitch.html', form = form)


@main.route('/add/comment<pitch_id>',methods = ['GET','POST'])
def add_comment(pitch_id):
    form = CommentForm()
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    if form.validate_on_submit():
        title = form.Title.data
        comment = form.comment.data
        new_comment = Comment(title = title, comment = comment, user = current_user, pitch = pitch)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('main.index'))
        
    return render_template('add_comment.html', form = form)

@main.route('/view/comment<pitch_id>',methods = ['GET','POST'])
def view_comment(pitch_id):
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id)
        
    return render_template('view_comment.html', comments = comments)





