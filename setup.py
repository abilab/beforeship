from setuptools import setup, find_packages

package_acoma = {
    'name': 'beforeship',
    'version': '0.1',
    'description': 'Before shipping app',
    'packages': find_packages(),
    'author': 'DreamTeam',
    'install_requires': [],

    # Always disable support for zip eggs
    'zip_safe': False,
}

setup(**package_acoma)
