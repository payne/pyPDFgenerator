import io
import re
from datetime import datetime, timezone

import markdown
from flask import Flask, jsonify, request, send_file
from weasyprint import HTML

app = Flask(__name__)

PLACEHOLDER_RE = re.compile(r"{{\s*(\w+)\s*}}")


def render_template(template: str, data: dict) -> str:
    return PLACEHOLDER_RE.sub(lambda m: str(data.get(m.group(1), m.group(0))), template)


@app.before_request
def log_request():
    print(f"[{datetime.now(timezone.utc).isoformat()}] {request.method} {request.path}", flush=True)


@app.get("/")
def index():
    return jsonify(
        message="Welcome to pyPDFgenerator! POST a template and data to /pdf to get your PDF.",
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.post("/pdf")
def generate_pdf():
    body = request.get_json(silent=True)
    if not body or "template" not in body:
        return jsonify(error="request body must include a 'template' field"), 400

    template = body["template"]
    data = body.get("data", {})

    markdown_text = render_template(template, data)
    html_body = markdown.markdown(markdown_text)
    pdf_bytes = HTML(string=html_body).write_pdf()

    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=True,
        download_name="document.pdf",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
