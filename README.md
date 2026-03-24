- The only dependency is ``python-dotenv``. You can install with

> pip install python-dotenv

> Substitute your ``TOKEN`` with your equivalent from [serper](https://serper.dev)

This code was made by me and it will be improved in the future for adding more features such as:

- Implement a TUI friendly interface
- Allowing to use AI to filter the final list to remove unwanted links
- Comments to increase readability
- More flexibility and support for different search engines

## What can this code be used for?

- Build your own list of most popular NSFW websites for blocking mechanisms.
- Find new websites you haven't seen before.
- Increase your search engine power with more searches in one place.
- Save data by making a short list of links instead of trying to find a dataset of links on the internet.
- You want to find recent links instead of old ones that are deprecated.

## What this code does?

- Searches across the internet using the [serper](https://serper.dev) API finding websites based on the query for an amount of times

- Makes sure every link is unique by not allowing any duplicate URLs.

## What it does not do:

- Automatic filtering on the websites you didn't want to be there
> For example, you might want to block NSFW websites, but you'll find non-nsfw websites like news articles, psychology posts and others. For these cases you will have to filter manually.

