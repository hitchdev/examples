# HitchStory Examples

This project contains complete examples for how
[HitchStory](https://hitchdev.com/hitchstory)
can be used to test, specify and document four
types of projects.

They are all to do list apps.

- [ ] Command line app (commandline)
- [ ] Python API (pythonapi)
- [X] REST API (restapi)
- [ ] Website (with playwright) (website)

These projects can be used to demonstrate:

* Acceptance Test Driven Development
* Stories that rewrite themselves
* Stories that generate markdown documentation


## Getting started

```bash
$ git clone https://github.com/hitchdev/examples.git
$ cd examples/restapi
$ ./key.sh make
```

## Run all tests

Try this first to see that everything runs:

```
$ ./key.sh regression
```

## Run singular test

This command can be used to drive development of new features.

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

* Using stories in the [story folder](https://github.com/hitchdev/examples/tree/main/restapi/story).
* And the [story->text template](https://github.com/hitchdev/examples/blob/main/restapi/hitch/docstory.yml).
* The documentation in the [docs](https://github.com/hitchdev/examples/tree/main/restapi/docs) folder is generated.

Running this command will regenerated the docs.

```
$ ./key.sh docgen
```


# About

All apps here are based upon
[this simple to do app](https://github.com/ovinokurov/ToDo).

If you'd like to introduce capabilities like these to your project, [contact me now](hitchdev.com/consulting) for a free consultation.
