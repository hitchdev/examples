from hitchstory import (
    StoryCollection,
    BaseEngine,
    exceptions,
    validate,
    no_stacktrace_for,
)
from hitchstory import GivenDefinition, GivenProperty, InfoDefinition, InfoProperty
from templex import Templex
from strictyaml import Optional, Str, Map, Int, Bool, Enum, load, MapPattern
from path import Path
from shlex import split
from templex import Templex
from commandlib import Command
import requests
import time
from playwright.sync_api import sync_playwright


class App:
    """Interact directly with the app via podman."""

    def __init__(self, podman):
        self._podman = podman

    def start(self):
        self._podman("run", "--rm", "-d", "--name", "app", "app").output()

    def wait_until_ready(self):
        # Really bad way to do it
        time.sleep(1)

    def stop(self):
        self._podman("stop", "app", "--time", "1").output()

    def logs(self):
        self._podman("logs", "app").run()


class PlaywrightServer:
    def __init__(self, podman):
        self._podman = podman

    def start(self):
        self._podman("run", "--rm", "-d", "--name", "playwright", "playwright").output()

    def wait_until_ready(self):
        time.sleep(1)

    def ws(self):
        output = self._podman("logs", "playwright").output()
        output = output.replace("Listening on", "").strip()
        return output

    def stop(self):
        self._podman("stop", "playwright", "--time", "1").output()


class Engine(BaseEngine):
    """Python engine for running tests."""

    def __init__(self, paths, rewrite=False):
        self._path = paths
        self._app = App(Command("podman").in_dir(self._path.project))
        self._playwright_server = PlaywrightServer(
            Command("podman").in_dir(self._path.project)
        )
        self._rewrite = rewrite

    def set_up(self):
        Command("podman", "container", "rm", "--all").output()
        self._app.start()
        self._app.wait_until_ready()
        self._playwright_server.start()
        self._playwright_server.wait_until_ready()
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.connect(self._playwright_server.ws())

    def load_website(self):
        page = self._browser.new_page()
        page.goto("http://localhost:5000")
        # page.screenshot(path=f'example-1.png')

    def tear_down(self):
        if hasattr(self, "_browser"):
            self._browser.close()
        if hasattr(self, "_playwright"):
            self._playwright.stop()
        self._playwright_server.stop()
        self._app.stop()

    def on_failure(self, result):
        self._app.logs()

    def on_success(self):
        if self._rewrite:
            self.new_story.save()
