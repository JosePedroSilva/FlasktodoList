from flask import render_template, redirect, flash, url_for, request
from app import app, db
from app.models import Note
from app.forms import NoteForm

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = NoteForm()
    if form.validate_on_submit():
        note = Note(content=form.content.data)
        db.session.add(note)
        db.session.commit()
        flash('Note saved')
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    notes = Note.query.order_by(Note.timestamp.desc()).paginate(
        page, app.config['NOTES_PER_PAGE'], False)
    next_url = url_for('index', page=notes.next_num) \
        if notes.has_next else None
    prev_url = url_for('index', page=notes.prev_num) \
        if notes.has_prev else None
    return render_template('index.html', notes=notes.items, 
        	    form=form, title='HomePage', next_url=next_url,
                           prev_url=prev_url)