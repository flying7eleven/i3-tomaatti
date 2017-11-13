from setuptools import setup, find_packages

setup(
	name='tomaatti',
	version='0.0.5.dev1',
	description='Pomodoro timer with i3 integration',
	long_description='Pomodoro timer with i3 integration',
	url='https://github.com/thuetz/i3-tomaatti',
	author='Tim Hütz',
	author_email='tim@huetz.biz',
	license='GPLv3',
	packages=find_packages(),
	install_requires=[],
	zip_safe=False,
	platforms=['Linux'],
	entry_points={
		'console_scripts': [
			'tomaatti = tomaatti.cli:script_entry_point',
		],
	}
)
