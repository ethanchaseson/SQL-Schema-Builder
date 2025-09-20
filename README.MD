# SQL Schema Builder

A Python tool that converts JSON or YAML schema definitions into SQL `CREATE TABLE` statements.

## Features
- Accepts JSON or YAML schema input
- Generates clean, valid SQL `CREATE TABLE` statements
- Modular design for easy extension
- Ready to integrate into CLI workflows or pipelines

## Installation
Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/yourusername/sql-schema-builder.git
cd sql-schema-builder
python3 -m venv .venv
source .venv/bin/activate   # On Windows use: .venv\Scripts\Activate.ps1
pip install -r requirements.txt

