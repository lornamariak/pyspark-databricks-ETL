# main file for terminal ops
# cli.py
#!/usr/bin/python
from dblib.selectdb import selectdb
from dblib.querydb import query
import click


@click.group
def main():
    pass


# click to select preferred database
@main.command()
@click.option("--database", prompt="Database name", help="Choose a database to query")
def dbselect(database):
    selectdb(database)


# click to select query
@main.command()
@click.option("--limit", prompt="Limit", help="Query a database")
@click.argument("tablename")
def tableselect(limit, tablename):
    query(tablename, limit)


if __name__ == "__main__":
    main()
