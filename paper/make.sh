docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja uplatex thesis.tex
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja dvipdfmx thesis.dvi
