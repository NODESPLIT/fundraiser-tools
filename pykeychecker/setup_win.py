from distutils.core import setup
import py2exe

data_files = ["logo.gif"]
setup(
	data_files=data_files,
	options={
		"py2exe" : {
			"includes" : "bitcoin,pyblake2,pysodium,appJar"
		}
	},
	console=['keychecker.py']
)