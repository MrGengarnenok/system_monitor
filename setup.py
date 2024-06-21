from setuptools import setup, find_packages

setup(
    name='system_monitor',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'rich'
    ],
    entry_points={
        'console_scripts': [
            'systeminfo=system_monitor.systeminfo:display_system_info',
        ],
    },
)

