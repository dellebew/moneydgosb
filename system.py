# -*- coding: utf-8 -*-
__author__ = 'Nikolay Mamashin (mamashin@gmail.com)'

from os import getppid
from settings import get_settings

cfg = get_settings()


async def first_run() -> bool:
    """Check if this is the first run of service. ppid is the parent process id.
    Save ppid to redis and check it on next run. If ppid is the same - this is not the first run."""
    ppid = getppid()
    return True
