# SQL Schema Builder

A Python-based tool that converts structured input (JSON or YAML) into SQL schema creation scripts. Designed to help developers, students, and data engineers rapidly prototype relational database schemas without memorizing SQL syntax.

---

## 🚀 Project Goals

- Strengthen understanding of relational database design
- Reinforce structured thinking through JSON/YAML parsing
- Build trust in conceptual clarity over rote memorization
- Create a modular, extensible tool for generating SQL scripts

---

## 🧠 Features

- Accepts JSON or YAML input describing tables and columns
- Generates `CREATE TABLE` statements for each defined table
- Supports basic data types (INT, VARCHAR, TEXT, DATE, etc.)
- Easy to extend with foreign keys, constraints, and sample data

---

## 📦 Input Format

### JSON Example
```json
{
  "users": [
    {"name": "id", "type": "INT PRIMARY KEY"},
    {"name": "username", "type": "VARCHAR(50)"},
    {"name": "email", "type": "VARCHAR(100)"}
  ],
  "posts": [
    {"name": "id", "type": "INT PRIMARY KEY"},
    {"name": "user_id", "type": "INT"},
    {"name": "content", "type": "TEXT"}
  ]
}
