# neo4j-CMS

This is a CLI neo4j CMS tool for [my website](https://aps.web.id/). Its a nice little tool I've been using. To install it you need to create a \_\_secret\_\_.py file in the following format:

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
- Create a \_\_secret\_\_.py file with the format above.
- I recommend using [pipenv](https://pipenv.pypa.io/en/latest/), install using `pipenv install --editable .` inside the cloned folder.


# Usage
Commands:
  - post-delete
  - post-list
  - post-update
  - post-write

You can write, delete, update, and list the existing posts in your neo4j database.

TODO:
- [x] add function to create a content folder
- [ ] explanation on how it works on the website
