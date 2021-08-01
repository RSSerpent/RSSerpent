import os
from dataclasses import dataclass

from hypothesis import settings


settings.register_profile("ci", max_examples=200)
settings.register_profile("default", max_examples=50)

settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))


@dataclass
class Times:
    """
    Data class for storing constants, specifying how many times a `hypothesis` \
    test shoul run.

    * `ONCE` for tests that only need to be run once;
    * `SOME` for tests that are meant to be mildly tested;
    * `THOROUGH` for tests that are meant to be thoroughly tested.
    """

    ONCE = 1
    SOME = settings.default.max_examples // 3
    THOROUGH = settings.default.max_examples
