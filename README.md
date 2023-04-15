# HitchStory Examples

[![Example Tests Running on Github Actions](https://github.com/hitchdev/examples/actions/workflows/regression.yml/badge.svg)](https://github.com/hitchdev/examples/actions/workflows/regression.yml)

This project contains complete examples for how
[HitchStory](https://hitchdev.com/hitchstory)
can be used to testing and living documentation framework:

- [X] REST API (restapi)
- [X] Website (with playwright) (website)
- [X] Command line app (commandline)
- [ ] Python API (pythonapi)

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
$ cd examples/[ RELEVANT PROJECT FOLDER ]
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
Command Line | [stories](https://github.com/hitchdev/examples/tree/main/commandline/story) | [template](https://github.com/hitchdev/examples/blob/main/commandline/hitch/docstory.yml) | [docs](https://github.com/hitchdev/examples/tree/main/commandline/docs) 

Running this command in any of the above project folders will regenerate the docs for that project.

```
$ ./key.sh docgen
```


## Clean everything

This will everything created to run these tests (container/volume):

```
$ ./key.sh clean all
```

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
