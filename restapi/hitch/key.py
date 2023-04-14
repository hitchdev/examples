from hitchstory import StoryCollection
from click import argument, group, pass_context
from commandlib import Command
from engine import Engine
from pathlib import Path


class DIR:
    """All relevant directories"""
    key = Path(__file__).absolute().parents[0]
    project = Path(__file__).absolute().parents[0].parent
    story = Path(__file__).absolute().parents[0] / "story"


@group(invoke_without_command=True)
@pass_context
def cli(ctx):
    """Integration test command line interface."""
    pass


def _storybook(**settings):
    """Get all stories available to run with settings (e.g. rewriting)"""
    return StoryCollection(DIR.story.glob("*.story"), Engine(DIR, **settings))


@cli.command()
@argument("keywords", nargs=-1)
def ratdd(keywords):
    """
    Run story with name containing keywords and rewrite.
    """
    _storybook(rewrite=True).shortcut(
        *keywords
    ).play()


@cli.command()
@argument("keywords", nargs=-1)
def atdd(keywords):
    """
    Run story with name containing keywords.
    """
    _storybook().shortcut(*keywords).play()


@cli.command()
def regression():
    """
    Run all child tests.
    """
    _storybook().only_uninherited().ordered_by_name().play()


@cli.command()
def build():
    Command("podman", "build", ".", "-t", "app").in_dir(DIR.project).run()


if __name__ == "__main__":
    cli()
