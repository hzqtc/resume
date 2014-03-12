all: index.html

index.html: zhiqiang-huang.md views/layout.html
	./build.py zhiqiang-huang.md index.html

.PHONY: clean

clean:
	rm -f *.html
