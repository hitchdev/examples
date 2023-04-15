# HitchStory Examples

[![Example Tests Running on Github Actions](https://github.com/hitchdev/examples/actions/workflows/regression.yml/badge.svg)](https://github.com/hitchdev/examples/actions/workflows/regression.yml)

This project contains complete examples for how
[HitchStory](https://hitchdev.com/hitchstory)
can be used to test, specify and document four
types of projects.

They are all to do list apps.

- [X] REST API (restapi)
- [X] Website (with playwright) (website)
- [ ] Command line app (commandline)
- [ ] Python API (pythonapi)

These projects can be used to demonstrate:

* Acceptance Test Driven Development
* Stories that rewrite themselves
* Stories that generate markdown documentation


## Getting started

```bash
$ git clone https://github.com/hitchdev/examples.git
```

Go to the relevant project folder:

```bash
$ cd examples/restapi
```

OR

```bash
$ cd examples/website
```

```bash
$ ./key.sh make
```

## Run all tests

Try this first to see that everything runs:

```
$ ./key.sh regression
```

## Run singular test

This command can be used to acceptance test driven development.

```
$ ./key.sh atdd correct
```

## Run singular test in rewrite mode

Try changing the code to output something different and run this to 
see the story rewrite itself:

```
$ ./key.sh ratdd correct
```

## Generate documentation from stories

Project | Stories | Story->Markdown Template | Markdown Docs
---|---|---|---
REST API | [stories](https://github.com/hitchdev/examples/tree/main/restapi/story) | [template](https://github.com/hitchdev/examples/blob/main/restapi/hitch/docstory.yml) | [docs](https://github.com/hitchdev/examples/tree/main/restapi/docs) 
Website | [stories](https://github.com/hitchdev/examples/tree/main/website/story) | [template](https://github.com/hitchdev/examples/blob/main/website/hitch/docstory.yml) | [docs](https://github.com/hitchdev/examples/tree/main/website/docs) 

Running this command will regenerated the docs.

```
$ ./key.sh docgen
```


# About

The tests are all based on
[this great little to do app](https://github.com/ovinokurov/ToDo)
built by [Oleg Vinokurov](https://github.com/ovinokurov) which was built
with a CLI, REST and web interface.

If you'd like to introduce capabilities like these to your project, [contact me now](hitchdev.com/consulting) for a free consultation.
