#!/usr/bin/env python3

import click
from dblib.selectdb import selectdb
from dblib.querydb import query
from dblib.sampler import summary
from dblib.sampler import sampler

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


@main.command
@click.option("--limit", prompt="Limit", help="Summarize")
#@click.option("--tablename", prompt = "please enter the tablename")
@click.argument("tablename")
def summarize(tablename, limit):
    summary(tablename, limit)



@main.command
@click.option("--limit", prompt="Limit", help="Sampler")
@click.option("--n",prompt="Sample size", help="Sampler")
@click.argument("tablename")
def sample(tablename,limit,n):
    sampler(tablename,limit,n)


if __name__ == "__main__":
    main()
