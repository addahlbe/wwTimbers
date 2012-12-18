from setuptools import setup

entry_points = """
    [paste.app_factory]
    main = wwtimbersApp:main
"""

requires = [
    'pyramid',
    'waitress',
    'sqlalchemy'
]

setup(name='wwtimbersApp',
      version='0.0.1',
      description='Power Hour Drinking Game App',
      install_requires=requires,
      packages=['wwtimbersApp'],
      entry_points=entry_points
)
