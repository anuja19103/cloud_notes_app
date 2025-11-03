# Cloud Notes App

A tiny Flask-based notes app (in-memory) for development and testing.

Files created:
- `app.py` — minimal Flask app and routes (index, add, edit, delete)
- `templates/index.html` — list notes UI
- `templates/add_note.html` — add-note form
- `templates/edit_note.html` — edit-note form
- `requirements.txt` — Python dependencies

Running locally (PowerShell)

1. Create a virtual environment and activate it:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies and run:

```powershell
pip install -r requirements.txt
# Run the app locally
python .\app.py
```

Database and cloud notes
- The app uses SQLAlchemy and respects the `DATABASE_URL` environment variable. If `DATABASE_URL` is not set the app will create a local SQLite file `notes.db`.

Render deployment

1. Push your repository to GitHub.
2. On Render, create a new **Web Service**, connect your repo and choose the branch to deploy.
3. Set these values on the Render web service setup:
	- **Environment**: Python 3
	- **Build Command**: pip install -r requirements.txt
	- **Start Command**: gunicorn app:app
4. (Optional) If you plan to use a managed Postgres database on Render, add the `DATABASE_URL` environment variable Render provides to your service environment.

Procfile

I added a `Procfile` with `web: gunicorn app:app` so you can set the same start command locally or on other PaaS providers.

Notes
- The app now uses a database (SQLite by default). If you deploy to Render and connect a Postgres instance, Render will provide a `DATABASE_URL` env var — the app will use it.

Next steps
- Add simple authentication to let each user have their own notes.
- Add basic tests (pytest + Flask test client).
