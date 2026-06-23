# Interactions Log

## 2026-06-23

- Request: track all interactions in this file; build a RESTful webservice
  that generates a PDF from a POST body of the form
  `{ "template": "<markdown with {{placeholders}}>", "data": { ... } }`.
- Found project directory was empty aside from an unpopulated `venv`
  (Python 3.11.2) and a `.claude/settings.local.json`.
- Built `app.py`: a Flask app exposing `POST /pdf`. It substitutes
  `{{key}}` placeholders in the template using the `data` dict, renders the
  result as Markdown to HTML, converts the HTML to a PDF with WeasyPrint,
  and streams the PDF back as `application/pdf`.
- Installed `flask`, `markdown`, `weasyprint` into the existing venv and
  pinned them in `requirements.txt`.
- Verified end-to-end: started the dev server, POSTed the exact sample
  payload from the request, confirmed a valid PDF (v1.7) came back, and
  extracted its text to confirm the placeholders were substituted correctly
  ("Hi Matt Payne", "Welcome to W2 town", "Your job is Obey"). Used
  `pdfminer.six` only as a throwaway verification tool, then uninstalled it
  and its transitive deps (`charset-normalizer`, `cryptography`) so they
  don't pollute `requirements.txt`.
- Stopped the test server after verification; added `README.md` with setup,
  run, and example `curl` instructions.
- Request: add a friendly response for `GET /`.
- Added a `GET /` route returning a JSON welcome message pointing users to
  `POST /pdf`. Verified with a live server + `curl`, then stopped the
  server.
