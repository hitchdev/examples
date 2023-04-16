# HitchStory Examples

[![Example Tests Running on Github Actions](https://github.com/hitchdev/examples/actions/workflows/regression.yml/badge.svg)](https://github.com/hitchdev/examples/actions/workflows/regression.yml)

This project contains complete examples for how
[HitchStory](https://hitchdev.com/hitchstory)
can be used as a testing and living documentation framework:

Project | Tools used | Cool Features
---|---|---
REST API | requests | [Autogenerated docs](https://github.com/hitchdev/examples/tree/main/restapi/docs), Self rewriting stories
Website | playwright | [Autogenerated docs with videos and pictures](https://github.com/hitchdev/examples/tree/main/website/docs)
Command line app | icommandlib | [Autogenerated docs](https://github.com/hitchdev/examples/tree/main/commandline/docs), Self rewriting stories
Python API | hitchrunpy | [Autogenerated docs](https://github.com/hitchdev/examples/tree/main/pythonapi/docs), Self rewriting stories

These projects show of various aspects of the framework including:

* Acceptance Test Driven Development
* Stories that rewrite themselves
* Stories that autogenerate markdown documentation, demonstrating [triality](https://hitchdev.com/hitchstory/approach/triality/).

HitchStory is entirely open source and free to use.

If you'd like help with introducing capabilities like these to your project, [contact me now](hitchdev.com/consulting) for a free consultation.

## Getting started

All functionality is automated and can be run via one of the key.sh
scripts. **Podman must be installed on your system first though.**

```bash
$ git clone https://github.com/hitchdev/examples.git
$ cd examples/commandlib -OR- restapi -OR- website -OR- pythonapi
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

"correct" is a unique keyword used in the name of one of the stories.

## Run singular test in rewrite mode

You can try changing the code to output something different and run this to 
see the story rewrite itself:

```
$ ./key.sh ratdd correct
```

(Note: you make have to run `./key.sh build` first)

## Generate documentation from stories

Running this command in any of the above project folders will regenerate the docs for that project from the stories.

```
$ ./key.sh docgen
```

For the website project, the screenshots and video artefacts
used by the docs are retaken by running:

```
$ ./key.sh recordings
```


## Clean everything

This will destroy everything created to run these tests (container/volume):

```
$ ./key.sh clean all
```

Note that it must be run in each project folder.

# About the projects

The four folders contain four versions of the same project -
[this great little to do app](https://github.com/ovinokurov/ToDo)
built by [Oleg Vinokurov](https://github.com/ovinokurov) which was built
with a command line, REST and web interface.

The ./key.sh scripts runs the app in a container *inside* the hitch container.

This is done to segregate the test code from the application code.

The website also runs a separate playwright container inside the hitch container.

The hitch container is run with a "gen" volume. This is a podman volume that
contains all builds necessary to run the app.


# Future work on examples

- [X] Generate website images and videos with playwright for use in documentation.
- [ ] Mount code folder with podman so changes reflect instantaneously.
- [ ] Use postgres with to do apps, and demonstrate given preconditions to fill database.
- [ ] Mock the passage of time - to do app with reminder.
- [ ] Show off inheritance (e.g. with a logging in story for website).
