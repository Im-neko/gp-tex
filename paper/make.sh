docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:2018 platex thesis.tex
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:2018 dvipdfmx thesis.dvi
