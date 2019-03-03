from setuptools import setup, find_packages
import os
import subprocess


MAJOR = 0
MINOR = 0
PATCH = 1
RELEASE = False
VERSION = '%d.%d.%d' % (MAJOR, MINOR, PATCH)


def git_rev():
    # Gather the git commit hash to attach to a non-release version

    def _minimal_ext_cmd(cmd):
        # construct minimal environment
        env = {}
        for k in ['SYSTEMROOT', 'PATH', 'HOME']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        # LANGUAGE is used on win32
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        GIT_REVISION = out.strip().decode('ascii')
    except OSError:
        GIT_REVISION = "unknown"

    return GIT_REVISION


def get_full_version():
    # Get the full version number for this application
    full_version = VERSION
    git_revision = git_rev()

    if not RELEASE:
        full_version += '.' + git_revision[:7]

    return full_version


dependencies = [
    'pyyaml'
]

setup(
    name='py-load',
    version=get_full_version(),
    author='Lane Terry',
    author_email='lane.terry@laneterry.com',
    url='https://lane.terry@laneterry.com',
    license='http://www.apache.org/licenses/LICENSE-2.0',
    description='A python based load testing framework',
    packages=find_packages(),
    install_requires=dependencies,
    setup_requires=['pytest-runner'],
    tests_require=['pytest']
)
