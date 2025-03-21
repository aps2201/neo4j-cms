# neo4j-CMS

This is a CLI neo4j CMS tool for my website. Its a nice little tool I've been using. To use it you need to create a \_\_secret\_\_.py file 

```
neo4j_cred = dict(
    NEO4J_URI= [neo4j aura URL],
    NEO4J_USERNAME= [neo4j db username],
    NEO4J_PASSWORD= [neo4j db password],
    AURA_INSTANCEID= [neo4j aura instance ID],
    AURA_INSTANCENAME= [neo4j aura instance name]
)
```

you can get a free instance from the [neo4j Aura site](https://console.neo4j.io/)

# Installation

- Clone this repo. 
- I recommend using pipenv, install using `pipenv install --editable .` inside the `cms` folder in the cloned folder.


## alternative
You can use [uv](https://github.com/astral-sh/uv) as well, just install uv and do `uv add --editable .` inside the `cms` folder.

# Usage

Within the active environment just write `cms [command]` most of it is self explanatory. If using uv, write `uv run cms`.

Commands:
  - post-delete
  - post-list
  - post-update
  - post-write

You can write, delete, update, and list the existing posts in your neo4j database.

# How It Works

This is a very simple app that reads and writes into a [neo4j auradb](https://neo4j.com/product/auradb/) database. It sets up a post by writing:
- created date
- author
- modified date (if applicable)
- source
- category* (planned)

The `post-write` function needs a text file as an input so you would need to provide a path to that text file. It doesn't really do much, the markdown is processed at the web application. This  one is ingested by a flask framework and rendered using [python-markdown](https://python-markdown.github.io/).

The `post-update` downloads the file as a markdown file (.md) into a `content` folder -- if it is not available the cms will create one for you in the working directory -- where you can edit it. Once done you can confirm  the prompt, choose to change the title or not.