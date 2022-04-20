#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

# Status Badges
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_anybadge')

name = "370-470_Activity_4"

default_task = [
    'publish',
    'anybadge'
]

@init
def set_properties(project):
    project.build_depends_on('coverage')