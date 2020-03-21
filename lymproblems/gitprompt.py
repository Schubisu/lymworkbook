# The user will install bash-git-prompt, following the instructions on
# https://github.com/magicmonty/bash-git-prompt, and then update the `PATH`
# variable in such a way so that `gitprompt.sh` is available.

import os
import sys
from .utils import system, success, fail


def setup():
    "Setup gitprompt"
    pass  # Nothing to do.


def verify():
    "Verify gitprompt"
    gitprompt = os.path.join(os.environ["HOME"], ".bash-git-prompt/gitprompt.sh")
    if not os.path.exists(gitprompt):
        fail("Cannot find `gitprompt.sh` in the right location.")
    if "GIT_BRANCH" not in os.environ.keys():
        fail("Cannot verify that `gitprompt.sh` has been sourced correctly.")

    # if everything okay, then
    success()
