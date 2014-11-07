#!/usr/bin/env python
import optparse
import os

def main():
	p = optparse.OptionParser()
	p.add_option('--xcactivity-files-dir', '-x', help="Directory where .xcactivity files are located")
	p.add_option('--file', '-f', help="File for which parameters are searching for")

	options, arguments = p.parse_args()
	if not options.xcactivity_files_dir:
		p.error("xcode activity directory path required")

	if not options.file:
		p.error("searching file path is required")

	# Check that file starts from backslash
	if not options.file.startswith("/")	:
		p.error("Provide full path to the file")

	# Check that directory exists
	if not os.path.exists(options.xcactivity_files_dir) or not os.path.is_dir(options.xcactivity_files_dir):
		p.error("Specified directory doesn't exist")

	print 'Hello %s' % options.path

if __name__ == '__main__':
	main()