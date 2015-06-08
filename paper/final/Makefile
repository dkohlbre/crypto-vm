.PHONY: final.pdf

final.pdf: *.tex final.bbl final.bib
	pdflatex final.tex
	-if grep "undefined references" final.log; \
		then bibtex final; pdflatex final.tex; fi
	-if grep "may have changed" final.log; \
		then pdflatex final.tex; fi

final.bbl: final.bib
	pdflatex final.tex
	bibtex final
	pdflatex final.tex

spell:
	cat *.tex | aspell -a --add-filter=tex | grep -v \* | cut -d\  -f2 | sort | uniq | cat -s

clean:
	rm -f final.pdf final.bbl final.aux final.log final.blg final.out
