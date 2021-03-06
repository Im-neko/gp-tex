#!/bin/bash
cd `dirname $0`

git config --global user.name "im-neko"
git config --global user.email "yuki@ideta.net"

git remote set-url origin https://im-neko:${GITHUB_TOKEN}@github.com/Im-neko/gp-tex.git

git checkout -b master
git pull origin master
git branch -a

git log -1

last_commit_message="$(git log -1 | tail -1)"
echo $last_commit_message
echo $PWD

docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:latest platex thesis.tex
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:latest pbibtex thesis
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:latest platex thesis.tex
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:latest platex thesis.tex
docker run --rm -v $PWD:/workdir paperist/alpine-texlive-ja:latest dvipdfmx thesis

echo '!paper/thesis.pdf' >> ../.gitignore
git add .
git commit -m '[updater] update pdf'
git push origin HEAD

