#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
#use_plugin("python.coverage")
use_plugin("python.distutils")
use_plugin("copy_resources")


name = "Bronco-Mates"
default_task = "publish"


@init
def set_properties(project):
    project.depends_on_requirements("requirements.txt")
    project.include_file("templates","*.html")