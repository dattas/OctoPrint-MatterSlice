# coding=utf-8
import setuptools

def package_data_dirs(source, sub_folders):
	import os
	dirs = []

	for d in sub_folders:
		for dirname, _, files in os.walk(os.path.join(source, d)):
			dirname = os.path.relpath(dirname, source)
			for f in files:
				dirs.append(os.path.join(dirname, f))

	return dirs

def params():
	name = "OctoPrint-MatterSlice"
	version = "0.1"

	description = "Adds support for slicing via MatterSlice from within OctoPrint"
	author = "Dattas Moonchaser"
	author_email = "dattasmoon@gmail.com"
	url = "http://octoprint.org"
	license = "AGPLv3"

	packages = ["octoprint_matterslice"]
	package_data = {"octoprint_matterslice": package_data_dirs('octoprint_matterslice', ['static', 'templates'])}

	include_package_data = True
	zip_safe = False
	install_requires = open("requirements.txt").read().split("\n")

	entry_points = {
		"octoprint.plugin": [
			"matterslice = octoprint_matterslice"
		]
	}

	return locals()

setuptools.setup(**params())
