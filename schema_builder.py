import json
import yaml
import os
import sys

def load_schema(file_path):
    """Load schema from JSON or YAML file."""
    ext = os.path.splitext(file_path)[1].lower()
    with open(file_path, 'r') as f:
        if ext == '.json':
            return json.load(f)
        elif ext in ['.yaml', '.yml']:
            return yaml.safe_load(f)
        else:
            raise ValueError("Unsupported file format. Use .json or .yaml")

def generate_sql(schema):
    """Generate SQL CREATE TABLE statements from schema dict."""
    statements = []
    for table_name, columns in schema.items():
        col_defs = []
        for col in columns:
            name = col.get('name')
            col_type = col.get('type')
            if not name or not col_type:
                raise ValueError(f"Missing 'name' or 'type' in table '{table_name}'")
            col_defs.append(f"  {name} {col_type}")
        sql = f"CREATE TABLE {table_name} (\n" + ",\n".join(col_defs) + "\n);"
        statements.append(sql)
    return "\n\n".join(statements)

def main():
    if len(sys.argv) != 2:
        print("Usage: python schema_builder.py <schema_file.json|yaml>")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        schema = load_schema(file_path)
        sql_output = generate_sql(schema)
        print(sql_output)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
