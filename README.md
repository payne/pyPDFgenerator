# pyPDFgenerator

RESTful service that turns a Markdown template + data dict into a PDF.

## Setup

```bash
source venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
source venv/bin/activate
python3 app.py
```

Server listens on `http://0.0.0.0:5000`.

## API

`POST /pdf`

Request body:

```json
{
  "template": "# Hi {{name}}\nWelcome to **{{company}}**\n\nYour job is {{job}}",
  "data": { "name": "Matt Payne", "company": "W2 town", "job": "Obey" }
}
```

`{{key}}` placeholders in `template` are substituted from `data`, the result is
rendered as Markdown, then converted to a PDF. Response is `application/pdf`
(`document.pdf`).

Example:

```bash
curl -X POST http://localhost:5000/pdf \
  -H "Content-Type: application/json" \
  -d '{"template":"# Hi {{name}}\nWelcome to **{{company}}**\n\nYour job is {{job}}","data":{"name":"Matt Payne","company":"W2 town","job":"Obey"}}' \
  -o document.pdf
```
