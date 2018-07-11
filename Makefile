FILENAME = resume
CC=platex
DD=dvipdfmx

docs/resume.pdf: ${FILENAME}.dvi
	$(DD) $<
${FILENAME}.dvi: ${FILENAME}.tex
	$(CC) $<

clean:
	rm -rf ${FILENAME}.aux ${FILENAME}.dvi ${FILENAME}.log
