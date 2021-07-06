import setuptools

setuptools.setup(
    name='robin_monitor',
    version='1.0.0',
    author='cruiser0631',
    description='IFTTT-like stock assistant for Robinhood.',
    packages=setuptools.find_packages(exclude=['docs']),
    include_package_data=True,
    url='http://github.com/mdw771/robin_monitor.git',
    keywords=['stock', 'robinhood'],
    license='BSD-3',
    platforms='Any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Operating System :: OS Independent',
    ]
)