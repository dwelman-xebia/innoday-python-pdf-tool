.PHONY: cleanup setup rotate merge 

cleanup:
	rm -rf output

setup:
	mkdir -p output

rotate: setup
	python3 -m pdftool.main testdata/with-images.pdf -o output/rotated.pdf -rot 1:180 -rot 2:90 -rot 3,4:-90

merge: setup
	python3 -m pdftool.main testdata/with-images.pdf -o output/merged.pdf -m testdata/with-images.pdf:2:2-3 -m testdata/with-images.pdf:-1

encrypt: setup 
	python3 -m pdftool.main testdata/with-images.pdf -o output/encrypted.pdf -e "my-encryption-key"

decrypt: setup encrypt 
	python3 -m pdftool.main testdata/with-images.pdf -o output/decrypted.pdf -d "my-encryption-key"

pages: setup 
	python3 -m pdftool.main testdata/with-images.pdf -o output/selection.pdf -p 1-2,4

remove: setup 
	python3 -m pdftool.main testdata/with-images.pdf -o output/remove.pdf -r 1-2,4

all: cleanup setup rotate merge encrypt decrypt pages remove