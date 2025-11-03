import os
from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Use DATABASE_URL if provided (e.g. from Render); otherwise fallback to sqlite
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///notes.db')
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Database model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)

    def __repr__(self):
        return f"<Note {self.id} {self.title}>"


@app.route('/')
def index():
    notes = Note.query.order_by(Note.id.desc()).all()
    return render_template('index.html', notes=notes)


@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if not title:
            return render_template('add_note.html', error='Title is required', title=title, content=content)
        new_note = Note(title=title, content=content)
        db.session.add(new_note)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_note.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        content = request.form.get('content', '').strip()
        if not title:
            return render_template('edit_note.html', note=note, error='Title is required')
        note.title = title
        note.content = content
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_note.html', note=note)


@app.route('/delete/<int:id>', methods=['POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # For local development
    app.run(debug=True, host='0.0.0.0')
