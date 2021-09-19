import os
from dataclasses import dataclass

import pytest
from hypothesis import settings
from starlette.testclient import TestClient

from rsserpent import app


settings.register_profile("ci", deadline=500, max_examples=200)
settings.register_profile("default", max_examples=50)

settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))


@dataclass
class Times:
    """Constants, specifying how many times a `hypothesis` test should run.

    * `ONCE` for tests that only need to be run once;
    * `SOME` for tests that are meant to be mildly tested;
    * `THOROUGH` for tests that are meant to be thoroughly tested.
    """

    ONCE = 1
    SOME = settings.default.max_examples // 3
    THOROUGH = settings.default.max_examples


@pytest.fixture(scope="module")
def client() -> TestClient:
    """Share one test client across the whole module with `pytest.fixture`."""
    return TestClient(app)
