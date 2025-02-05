from setuptools import setup

setup(
    name='CMS',
    version='0.0.9',
    py_modules=['cms_app','__secret__'],
    install_requires=[
        'Click', 'neo4j'
    ],
    entry_points={
        'console_scripts': [
            'cms = cms_app:cms'
        ],
    },
)
