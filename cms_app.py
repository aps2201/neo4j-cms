import click
from neo4j import GraphDatabase
from __secret__ import neo4j_cred
from datetime import datetime
from uuid import uuid4
import os


def content_dir():
    content_dir = "content"
    try:
        os.mkdir(content_dir)
        print("Created folder 'content'! Resuming.")
    except FileExistsError:
        print("Folder 'content' found. Resuming.")


def db_write(tx, *args, **kwargs):
    with GraphDatabase.driver(
            neo4j_cred['NEO4J_URI'],
            auth=(neo4j_cred['NEO4J_USERNAME'],
                  neo4j_cred['NEO4J_PASSWORD'])
    ) as driver:
        with driver.session() as session:
            session.execute_write(tx, *args, **kwargs)


def db_read(tx, *args, **kwargs):
    with GraphDatabase.driver(
            neo4j_cred['NEO4J_URI'],
            auth=(neo4j_cred['NEO4J_USERNAME'],
                  neo4j_cred['NEO4J_PASSWORD'])
    ) as driver:
        with driver.session() as session:
            result = session.execute_read(tx, *args, **kwargs)
    return result


@click.group()
def cms():
    pass


# list
def list_post(tx):
    result = tx.run(
        "MATCH (p:Post) "
        "RETURN p "
        "ORDER BY p.created;"
    )
    return result.data()


@cms.command()
def post_list():
    p = db_read(list_post)
    z = []
    for p in p:
        z.append(p["p"]["post_id"]+"||"+p["p"]["title"])
    return print(*[x+"\n" for x in z])


# write
def txt(text):
    with open(text, "r") as textfile:
        return textfile.read()


def write_post(tx, author, content, title, source):
    d = datetime.now()
    created = (str(d.year).rjust(4, '0')+str(d.month).rjust(2, '0') +
               str(d.day).rjust(2, '0')+str(d.hour).rjust(2, '0') +
               str(d.minute).rjust(2, '0')+str(d.second).rjust(2, '0')
               )
    return tx.run(
        "CREATE (p:Post {title:$title, content:$content, created:$created, "
        "post_id:$post_id, author:$author, source:$source}) ",
        author=author, content=content, title=title, created=created, post_id=str(uuid4()), source=source)


@cms.command()
@click.argument("content")
@click.option("--source", default="cms")
def post_write(content, source="cms"):
    content_dir()   
    content = txt(content)
    author = "2"
    title = click.prompt("Add Title::")
    db_write(write_post, author, content, title, source=source)


# update
def update_post_read(tx, post_id):
    result = tx.run(
        "MATCH (p:Post) WHERE p.post_id STARTS WITH $post_id "
        "RETURN p",
        post_id=post_id)
    return result.single().data()


def update_post_write(tx, post_id, content, title):
    d = datetime.now()
    modified = (str(d.year).rjust(4, '0') + str(d.month).rjust(2, '0') +
                str(d.day).rjust(2, '0') + str(d.hour).rjust(2, '0') +
                str(d.minute).rjust(2, '0') + str(d.second).rjust(2, '0')
                )
    tx.run(
        "MATCH (p:Post) WHERE p.post_id STARTS WITH $post_id "
        "SET p.title=$title, p.content=$content, p.modified=$modified ",
        content=content, title=title, modified=modified, post_id=post_id)


@cms.command()
@click.argument("post_id")
def post_update(post_id):
    content_dir()   
    post_to_update = db_read(update_post_read, post_id)
    default_title = post_to_update['p']['title']
    post_id = post_to_update['p']['post_id']
    content = post_to_update['p']['content']
    with open("content/"+default_title+"_"+post_id[0:8]+".md", "w") as post_file:
        post_file.write(content)
    click.confirm("Open "+"content/"+default_title+"_"+post_id[0:8]+".md"+", edit, and press enter when done")
    if click.confirm("Change Title "+post_to_update['p']['title']+"?"):
        title = click.prompt("New Title::", type=str)
    else:
        title = default_title
    with open("content/"+default_title+"_"+post_id[0:8]+".md", "r") as content:
        content = content.read()
    db_write(update_post_write, post_id, content, title)


def delete_post(tx, **kwargs):
    if kwargs['post_id'] is not None:
        tx.run(
            "MATCH (p:Post) WHERE p.post_id STARTS WITH $post_id "
            "DETACH DELETE p", post_id=kwargs['post_id']
        )
    elif kwargs['title'] is not None:
        tx.run(
            "MATCH (p:Post) WHERE p.title = $title "
            "DETACH DELETE p", title=kwargs['title']
        )
    else:
        pass


@cms.command()
@click.option("--post_id")
@click.option("--title")
def post_delete(**kwargs):
    click.confirm("Are you sure?", abort=True)
    db_write(delete_post, **kwargs)

