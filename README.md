# 🏎️ Car Manager CLI

A professional **CRUD (Create, Read, Update, Delete)** command-line application designed to manage vehicle and owner records.

This project showcases:
- Structured database management
- Clean code principles
- Robust CLI interaction

---

## 🛠️ Tech Stack

| Tool / Environment | Version        | Purpose                          |
|-------------------|---------------|----------------------------------|
| Python            | 3.10+         | Core logic & scripting           |
| SQLite3           | Standard Lib  | Local relational database        |
| Libraries         | sqlite3, os   | Database & OS interaction        |

---

## 📦 Features

- **Database Persistence**  
  Uses SQLite3 with automatic table creation on first run.

- **Security**  
  Implements parameterized queries (`?` placeholders) to prevent SQL injection.

- **Modern Python Syntax**  
  Utilizes `match-case` (Python 3.10+) for clean CLI navigation.

- **Data Integrity**  
  Uses `try-except-finally` blocks to ensure safe database connection handling.

---

## 🚀 Installation & Usage

### 1. Clone the repository
```bash
git clone https://github.com/samuelmafradev/Car-Manager-CLI.git
cd Car-Manager-CLI
```
### 2. Run Depository.
```bash
python main.py
```

## 📝 Additional Notes.
- Use a DB viewer to see the database, it will always be located on the root folder, after you execute main.py.
