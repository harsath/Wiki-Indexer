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
- `LOCAL_DB_NAME` - Preferred Sqlite output filename

## Crawl settings
### Health
```py
traversal_depth = 4
patterns_to_avoid = [r'^Health_law$', r'.*by_country$', r'^Physicians_from.*', r'.*by_nationality$', r'.*_practitioners$', r'.*_dentists$', r'.*homeopaths$', r'.*by_continent$', r'.*by_decade$', r'.*by_century$', r'.*_nurses$', r'.*_physicians$', r'.*_law$', r'.*midwives$', r'.*_researchers$']
master_category = "Health"
categories_to_traverse = ["Physical_fitness", "Quality_of_life", "Sexual_health", "Disability_by_type", "Health_disasters", "Education_and_health", "Health_economics", "Health_informatics", "Mental_health", "Medical_terminology", "Health_sciences"]
```
### Physics
```py

```
