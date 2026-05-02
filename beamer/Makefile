# Build all weekly Beamer PDFs (requires latexmk + LaTeX).
TEX := $(wildcard week*.tex)
PDF := $(TEX:.tex=.pdf)

.PHONY: all clean

all: $(PDF)

%.pdf: %.tex beamersettings.tex
	latexmk -pdf -interaction=nonstopmode -halt-on-error $<

clean:
	latexmk -c $(TEX)
	rm -f $(PDF)
