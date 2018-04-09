

## Interesting ideas

https://docs.scrapy.org/en/latest/topics/architecture.html

### Extension of css selectors

Then add ::text to fetch the text, or ::attr(href) to fetch an attribute on a dom node.


```
In [4]: response.css('li.next a').extract_first()
Out[4]: '<a href="/page/2/">Next <span aria-hidden="true">→</span></a>'

In [5]: response.css('li.next a::attr(href)').extract_first()
Out[5]: '/page/2/'
```

JSON lines - is a format for streaming json - each line is valid json, so you can leave the file open and append new entries


### Output handler is the Item Pipeline

You can output with `-o some-output-file.json` or `-o some-output-file.jl`

Or you can use a more involved pipeline processor to write to a DB.

