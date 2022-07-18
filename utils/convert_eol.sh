#!/usr/bin/env bash

git ls-files '**.sh' | xargs dos2unix
git ls-files '**.py' | xargs dos2unix
git ls-files '**.rst' | xargs dos2unix
git ls-files '**.txt' | xargs dos2unix
git ls-files '**.yml' | xargs dos2unix
git ls-files '**.md' | xargs dos2unix
git ls-files '**.cfg' | xargs dos2unix
git ls-files '**.python-version' | xargs dos2unix
git ls-files '**.gitignore' | xargs dos2unix
git ls-files '**.gitattributes' | xargs dos2unix
git ls-files 'LICENSE' | xargs dos2unix
git ls-files 'README' | xargs dos2unix
git ls-files 'CODEOWNERS' | xargs dos2unix
