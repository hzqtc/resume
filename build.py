#!/usr/bin/env python2

from jinja2 import Environment, Template, FileSystemLoader
import markdown
import sys
import codecs

def toCamelCase(str):
    return ' '.join(map(lambda x: x[0].upper() + x[1:], str.split(' ')))

if len(sys.argv) < 3:
    print "Usage: %s <markdown file> <html file>" % sys.argv[0]
    exit(1)

env = Environment(loader = FileSystemLoader('views'))
template = env.get_template("layout.html")

title = toCamelCase(sys.argv[1].split('.')[0].replace('-', ' '))
text = codecs.open(sys.argv[1], 'r', 'utf-8').read()
md = markdown.markdown(text)

with codecs.open(sys.argv[2], 'w', 'utf-8') as f:
    html = template.render(title = title, content = md)
    f.write(html)

