# Wiki Indexer

## Database
- Database dump: https://dumps.wikimedia.org/enwiki/latest/
    - Tables needed: `categorylinks`, `page`
- Database layout guide: https://www.mediawiki.org/wiki/Manual:Database_layout

## Environment
Create `.env` file with the following fields:
- `MYSQL_DB_USER` - Wiki DB username
- `MYSQL_DB_PASS` - Wiki DB password
- `MYSQL_DB_HOST` - Server's hostname/IP
- `MYSQL_DB_PORT` - server's listening port
- `MYSQL_DB_NAME` - Name of Wiki DB database
- `LOCAL_DB_NAME` - Sqlite3 output filename
