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
from playwright.sync_api import sync_playwright, expect
from slugify import slugify
from video import convert_to_slow_gif

# This lets IPython.embed play well with playwright
# since they both run an event loop
import nest_asyncio

nest_asyncio.apply()
# Use __import__('IPython').embed()


class App:
    """Run and interact with the web server."""

    def __init__(self, podman):
        self._podman = podman

    def start(self):
        self._podman("run", "--rm", "-d", "--name", "app", "app").output()
        self.wait_until_ready()

    def wait_until_ready(self):
        # Not ideal - should be replaced with port listener
        time.sleep(1)

    def stop(self):
        self._podman("stop", "app", "--time", "1").output()

    def logs(self):
        self._podman("logs", "app").run()


class PlaywrightServer:
    """
    Runs the server, grab a new page.
    """

    def __init__(self, podman):
        self._podman = podman

    def start(self):
        self._podman("run", "--rm", "-d", "--name", "playwright", "playwright").output()
        self.wait_until_ready()

    def wait_until_ready(self):
        # Not ideal - should be replaced with logs / port listener
        time.sleep(1)

    def _ws(self):
        output = self._podman("logs", "playwright").output()
        output = output.replace("Listening on", "").strip()
        return output

    def stop(self):
        if hasattr(self, "_browser"):
            self._browser.close()
        if hasattr(self, "_playwright"):
            self._playwright.stop()
        self._podman("stop", "playwright", "--time", "1").output()

    def new_page(self):
        self._playwright = sync_playwright().start()
        self._browser = self._playwright.chromium.connect(self._ws()).new_context(
            record_video_dir="videos/"
        )
        self._page = self._browser.new_page()
        self._page.set_default_navigation_timeout(10000)
        self._page.set_default_timeout(10000)
        return self._page


class Engine(BaseEngine):
    """Python engine for running tests."""

    info_definition = InfoDefinition(
        context=InfoProperty(schema=Str()),
    )

    def __init__(self, paths, rewrite=False, recordings=False):
        self._path = paths
        self._recordings = recordings
        self._rewrite = rewrite

        podman = Command("podman").in_dir(self._path.project)

        self._app = App(podman)
        self._playwright_server = PlaywrightServer(podman)

    def set_up(self):
        """Set up all tests."""
        self._app.start()
        self._playwright_server.start()
        self._page = self._playwright_server.new_page()

    def load_website(self):
        self._page.goto("http://localhost:5000")
        self._screenshot()

    def enter(self, on, text):
        self._page.get_by_test_id(slugify(on)).fill(text)

    def click(self, on):
        self._page.get_by_test_id(slugify(on)).click()

    def _screenshot(self):
        if self._recordings:
            self._page.screenshot(
                path=self._path.project
                / "screenshots"
                / "{}-{}-{}.png".format(
                    self.story.slug,
                    self.current_step.index,
                    self.current_step.slug,
                )
            )

    def should_appear(self, on, text, which=None):
        if which is None:
            item = self._page.get_by_test_id(slugify(on))
        else:
            which = 0 if which == "first" else int(which) - 1
            item = self._page.locator(".test-{}".format(slugify(on))).nth(which)
        expect(item).to_contain_text(text)
        self._screenshot()

    def pause(self):
        __import__("IPython").embed()

    def tear_down(self):
        """Tear down all tests"""
        if hasattr(self, "_playwright_server"):
            self._playwright_server.stop()
        if hasattr(self, "_app"):
            self._app.stop()

    def on_failure(self, result):
        """Run before teardown, only on failure."""
        if hasattr(self, "_page"):
            self._page.screenshot(
                path=self._path.project / "screenshots" / "failure.png"
            )
            self._path.project.joinpath("screenshots", "failure.html").write_text(
                self._page.content()
            )
            self._page.close()
            self._page.video.save_as(
                self._path.project / "screenshots" / "failure.webm"
            )
        if hasattr(self, "_app"):
            self._app.logs()

        # Clean up
        Command("podman", "container", "rm", "--all").output()

    def on_success(self):
        """Run before teardown, only on success."""
        self._page.close()

        if self._recordings:
            webm_path = self._path.project / "screenshots" / f"{self.story.slug}.webm"
            self._page.video.save_as(webm_path)
            convert_to_slow_gif(webm_path)

        if self._rewrite:
            self.new_story.save()
