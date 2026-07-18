# JSON Formatter

A lightweight utility for formatting and validating JSON documents.

The application loads JSON text, validates its syntax, formats it with indentation and prepares it for exporting.

---

## Example

Input

{"name":"Alice","age":25,"city":"Rome"}

Output

{
    "name": "Alice",
    "age": 25,
    "city": "Rome"
}

---

## Components

app.py
Application entry point.

loader.py
Loads JSON text.

validator.py
Checks JSON syntax.

formatter.py
Formats JSON.

exporter.py
Saves formatted content.

report.py
Displays processing summary.

Run

```bash
python app.py
```

Uses sample JSON bundled with the project.
