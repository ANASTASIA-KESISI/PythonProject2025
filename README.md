# 🃏 myJokes.py – JSON Joke Extractor & Interactive Bot

A Python script for interacting with remote joke services and JSON data files. Built as part of the MSc in Enterprise Software Systems Development – University of Macedonia (Course: Business Information Systems Lab, Instructor: Dr. Th. Mastoras).

---

## 📌 Description

This program processes jokes provided in JSON format, either by extracting them from local files or by interacting with a public online Joke API in real time.

It supports:

- **Extraction Mode** (`--extract <filename>`): Reads and parses jokes from a local JSON file.
- **Conversation Mode** (`--bot`): Interacts with the user via terminal and fetches jokes by category from a public API.

---

## 🧠 JSON Concepts

The project introduces structured data concepts using JSON, supporting:
- `single` type jokes (simple one-liners)
- `twopart` jokes (with `setup` and `delivery` fields)
- Basic error handling and validation
- Text logging of conversation mode session to `myJokes.log`

---

## ⚙️ Usage

### 1. Extraction Mode

```bash
$ python myJokes.py --extract 7.json
Setup: Why is Linux safe?
Punchline: Hackers peak through Windows only.
```

If the file is missing or invalid:

```bash
$ python myJokes.py --extract 14.json
Error: No such file!

$ python myJokes.py --extract 15.json
Error: Invalid JSON format!
```

---

### 2. Conversation Mode

```bash
$ python myJokes.py --bot
> What joke category would you like? Programming
Setup: Why do programmers always mix up Halloween and Christmas?
Punchline: Because Oct 31 == Dec 25!
```

Supported categories (case-sensitive):
- `Any`
- `Programming`
- `Misc`
- `Dark`
- `Pun`
- `Spooky`
- `Christmas`

💡 An empty response or invalid category will display proper error messages.

---

## 📁 Log Output

In `--bot` mode, all jokes are logged in a plain text file `myJokes.log`, which is **overwritten on each session**.

---

## 🔒 Error Handling

Includes `try-except` error handling for:
- Invalid file paths
- Malformed JSON
- Missing internet connection
- Unsupported categories
- Empty input

---

## 🧰 Dependencies

Only standard Python libraries are used:

```python
import sys
import json
import urllib.request
```

---

## 🧑‍💻 Author

**Anastasia Kesisi**  
🎓 MSc in Enterprise Software Systems Development  
📍 University of Macedonia

---

## 📎 License

This project is for educational purposes only and distributed under the MIT License.
