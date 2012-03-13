all: index.html index-cn.html

index.html: zhiqiang-huang.md views/layout.html
	./build.py zhiqiang-huang.md index.html

index-cn.html: zhiqiang-huang-cn.md views/layout.html
	./build.py zhiqiang-huang-cn.md index-cn.html

.PHONY: clean

clean:
	rm *.html
