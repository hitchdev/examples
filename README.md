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

Either:

```bash
$ cd examples/restapi
$ ./key.sh make
```

## Run all tests

```
$ ./key.sh regression
```

## Run singular test

```
$ ./key.sh atdd correct
```

## Run singular test

```
$ ./key.sh atdd correct
```

## Run singular test in rewrite mode

```
$ ./key.sh ratdd correct
```

## Generate documentation from stories

NOT AVAILABLE YET

```
$ ./key.sh docgen
```


# About

All apps here are based upon [this simple to do app](https://github.com/ovinokurov/ToDo).

If you'd like to introduce these advanced capabilities
on your project, [contact here now](hitchdev.com/consulting).
