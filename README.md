# Flask API & MongoDB Form Submission Project

This repository contains **two separate Flask applications** inside different folders:

- **Task 1 (`task1_flask_api`)** – A Flask app with `/api` route returning JSON data from a file, and an index page guiding the user.
- **Task 2 (`task2_flask_mongo_form`)** – A Flask app with a form that inserts data into MongoDB Atlas and displays a success or error message.

## Task 1 – Flask API Returning JSON from File

### Features
- `/` → Displays a welcome page with current time and a link to `/api`.
- `/api` → Returns JSON list from `data.json`.

### Setup
```bash
cd task1_flask_api
pip install -r requirements.txt
python app.py
```

### Visit:

- Index page → http://127.0.0.1:5000/
- API endpoint → http://127.0.0.1:5000/api


## Task 2 – Flask Form to MongoDB Atlas
### Features
- / → Displays a form to submit Name and Email.
- On success → Redirects to /success with "Data submitted successfully".
- On error → Displays error on the form page without redirection.
- Uses MongoDB Atlas for data storage.

### Setup
1. Update MongoDB connection string in .env
2. Install dependencies and run:
```bash
cd task2_flask_mongo_form
pip install -r requirements.txt
python app.py
```
3. Visit:
- Form → http://127.0.0.1:5000/
- Success page → http://127.0.0.1:5000/success

## Screenshots

Screenshots of both tasks are in the screenshots/ folder:

- task1_index_page.png - Welcome page with link to /api
- task1_api_output.png - API JSON output
- task2_form_submission.png – Form before submission
- task2_success_page.png – Success page