
## Title: Using Scrapy to check top sites in Alex

### Status: accepted

### Context:

We need to fetch data from an API. The API has concurrency limits, and some of these requests will fail, and need to be retried.

We also need to be able to store this data in a structured fashion.

We also want to deploy somewhere external, so a long running job doesn't rely on a laptop being open and not used for anything else.

We don't want to be locked in, so as much of it as possible should be opensource

### Decision: try using Scrapy

Scrapy is designed for crawling larger numbers of sites, where failures handled gracefully, and the data stored in a structured fashion. It's also open source.


### Consequences: 

Can be deployed conventially, or by using scraping hub.

We need to invest in learning how to use Scrapy, which will take some time, as it's a whole framework.

We have a more standaridised framework for scraping, so finding others to use it should be easier than teaching them a hand-rolled one.



