.SUFFIXES: .py .eps .pdf .svg

PY  = $(wildcard *py)
EPS = $(wildcard *eps)
PDF = $(wildcard *pdf)
SVG = $(wildcard *svg)

.py.eps:
	python $<

.eps.pdf:
	epstopdf $<

.pdf.svg:
	pdf2svg $< $@
	cp $< ../src/images
	cp $@ ../src/images

eps: $(EPS)
pdf: $(PDF)
svg: $(SVG)

all: svg 

