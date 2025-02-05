# neo4j-CMS

This is a CLI neo4j CMS tool for my website. Its a nice little tool I've been using. To use it you need to create a __secret__.py file 

```
neo4j_cred = dict(
    NEO4J_URI= [neo4j aura URL],
    NEO4J_USERNAME= [neo4j db username],
    NEO4J_PASSWORD= [neo4j db password],
    AURA_INSTANCEID= [neo4j aura instance ID]
    AURA_INSTANCENAME= [neo4j aura instance name]
)
```

you can get a free instance from the [neo4j Aura site](https://console.neo4j.io/)

# Installation

- Clone this repo. 
- I recommend using pipenv, install using `pipenv install --editable .` inside the cloned folder.


# Usage
Commands:
  post-delete
  post-list
  post-update
  post-write

You can write, delete, update, and list the existing posts in your neo4j database.