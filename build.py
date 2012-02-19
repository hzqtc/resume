#!/usr/bin/env python2

from jinja2 import Environment, Template, FileSystemLoader
import markdown
import sys

def toCamelCase(str):
	return ' '.join(map(lambda x: x[0].upper() + x[1:], str.split(' ')))

if len(sys.argv) < 3:
	print "Usage: %s <markdown file> <html file>" % sys.argv[0]
	exit(1)

env = Environment(loader = FileSystemLoader('views'))
template = env.get_template("layout.html")

title = toCamelCase(sys.argv[1].split('.')[0].replace('-', ' '))
text = open(sys.argv[1]).read()
md = markdown.markdown(text)

with open(sys.argv[2], 'w') as f:
	f.write(template.render(title = title, content = md))

