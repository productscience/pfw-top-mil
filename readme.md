# PFW-Top-Mil

This is the repo is for a screenscaper I'm working on, to help me work out how much of the web we use runs on renewable power.

Or, more specficially how many of the top million websites as ranked by Alexa run on renewable power.

I'm not sure the best way to to this, but there's an API provied by the GreenWeb foundation that lets you do _some_ of this. I've written a bit more here, with this [jupyter notebook explaining my thinking in more detail](https://github.com/productscience/planet-friendly-web/blob/hugo/binder/how-much-web-renewable.ipynb).

Anyway, once you get over the abject terror of it all, learning something new in the open is a nice way to get input from the combined knowledge of everyone who knows more than you about a domain.

### Goals of this project

- work out how many of the top million websites as ranked by Alexa run on renewable power
- to work out a polite, sensible way to hit an API a million times in a reasonably efficient way
- to learn a bit more about screenscraping


### Installation 

This project runs on python 3, and uses `pipenv` to manage dependencies. Please see refer to the [pipenv documentation](https://docs.pipenv.org/) for installation and running the project - if you haven't used it yet, I _really_ recommend it.

```

pipenv shell
```


### Getting the Data

The results of running this to check the top 100k domains are available on [Datbase](https://datbase.org/view?query=8be6d29e63b010bb4240dc366e578e1f7f91e89a73062a7802c5b83d9cc793fe
) now, at the link below:

https://datbase.org/view?query=8be6d29e63b010bb4240dc366e578e1f7f91e89a73062a7802c5b83d9cc793fe

You can download it by visiting the website at the link above.

You can subscribe to always have the latest version of the data by downloading it with [Dat](http://datproject.org/).
