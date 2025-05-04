from sqlalchemy import create_engine, text
import sqlite3
import re
import os
from dotenv import load_dotenv
from config import CONFIG

selected_config = "biology"
config = CONFIG[selected_config]

# Load environment variables from .env file
load_dotenv()

# Database connection details from .env
user = os.getenv("MYSQL_DB_USER")
password = os.getenv("MYSQL_DB_PASS")
host = os.getenv("MYSQL_DB_HOST")
port = os.getenv("MYSQL_DB_PORT")
database = os.getenv("MYSQL_DB_NAME")
local_db_name = os.getenv("LOCAL_DB_NAME", "wiki_categories.db")

mysql_engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}", echo=False)

# Traversal details

def setup_sqlite():
    conn = sqlite3.connect(local_db_name)
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS category (
        category_id INTEGER PRIMARY KEY AUTOINCREMENT,
        category_name VARCHAR(255) UNIQUE
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        article_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category_name VARCHAR(255),
        FOREIGN KEY (category_name) REFERENCES category(category_name),
        UNIQUE (name, category_name)
    )
    ''')
    
    conn.commit()
    return conn, cursor

def category_traversal_dfs(category_name, sqlite_cursor, mysql_connection, visited, levels_deep):
    if any(re.search(pattern_to_avoid, category_name) for pattern_to_avoid in config.patterns_to_avoid):
        return
    if levels_deep <= 0:
        return
    if category_name in visited:
        return
    visited.add(category_name)
    print(f"current category: {category_name}")
    articles_in_current_category = text("""
        SELECT page_title 
        FROM categorylinks cl 
        JOIN page p ON cl.cl_from = p.page_id 
        WHERE cl.cl_to = :cat AND p.page_namespace = 0
    """)
    subcategories_in_current_category = text("""
        SELECT page_title 
        FROM categorylinks cl 
        JOIN page p ON cl.cl_from = p.page_id 
        WHERE cl.cl_to = :cat AND p.page_namespace = 14
    """)

    articles_in_current_category_result = mysql_connection.execute(articles_in_current_category, {"cat": category_name})
    for row in articles_in_current_category_result:
        article_name = row[0].decode("utf-8")
        try:
            sqlite_cursor.execute(
                "INSERT INTO articles (name, category_name) VALUES (?, ?)",
                (article_name, config.master_category)
            )
        except sqlite3.IntegrityError:
            pass
    
    subcategories_in_current_category_result = mysql_connection.execute(subcategories_in_current_category, {"cat": category_name})
    for row in subcategories_in_current_category_result:
        category_traversal_dfs(row[0].decode("utf-8"), sqlite_cursor, mysql_connection, visited, levels_deep - 1)

def main():
    sqlite_conn, sqlite_cursor = setup_sqlite()
    visited = set()
    
    with mysql_engine.connect() as conn:
        try:
            sqlite_cursor.execute(
                "INSERT INTO category (category_name) VALUES (?)",
                (config.master_category,)
            )
            sqlite_conn.commit()
        except sqlite3.IntegrityError:
            pass
        
        for category_name in config.categories_to_traverse:
            category_traversal_dfs(category_name, sqlite_cursor, conn, visited, config.traversal_depth)
        sqlite_conn.commit()
    
    sqlite_conn.close()

if __name__ == "__main__":
    main()

