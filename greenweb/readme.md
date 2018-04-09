### GreenWeb Scraper

## Rough steps

- set up what structured info we want to fetch with our spiders
- set up spider
- set up pipeline to persist data
- tune concurrency, to avoid cooking the API server
- deploy

### Set up Items 

Setting this up is straightforward enough. You can serialise the data coming back from the fields, to turn a date into a string for example

### Set up Spider




### Setup Item Pipeline

Make the spider generate a list of urls to parse.

You can run this locally to generate a set of json lines like so

```
scrapy crawl green_or_not -o green_or_not.jl
```


