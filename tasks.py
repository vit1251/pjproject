
from invoke import task
from os.path import exists

@task
def automake(c):
    """ Prepare ninja make scenario
    """
    if not exists('builddir'):
        c.run('CC=clang meson builddir', echo=True, pty=True)

@task(pre=[automake])
def clean(c):
    c.run('ninja -C builddir clean', echo=True, pty=True)

@task(default=True, pre=[automake])
def build(c):
    """ Source code compile routine
    """
    c.run('ninja -C builddir', echo=True, pty=True)
