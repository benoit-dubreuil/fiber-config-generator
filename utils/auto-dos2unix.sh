#!/usr/bin/env bash

# This script must be executed in a directory which belongs to a Git repository.

git ls-files '**.sh' | xargs dos2unix
git ls-files '**.py' | xargs dos2unix
git ls-files '**.pyc' | xargs dos2unix
git ls-files '**.python-version' | xargs dos2unix
git ls-files '**.c' | xargs dos2unix
git ls-files '**.h' | xargs dos2unix
git ls-files '**.cpp' | xargs dos2unix
git ls-files '**.hpp' | xargs dos2unix
git ls-files '**.d' | xargs dos2unix
git ls-files '**.java' | xargs dos2unix
git ls-files '**.cs' | xargs dos2unix

git ls-files '**.yml' | xargs dos2unix
git ls-files '**.xml' | xargs dos2unix
git ls-files '**.toml' | xargs dos2unix
git ls-files '**.json' | xargs dos2unix
git ls-files '**.properties' | xargs dos2unix
git ls-files '**.cfg' | xargs dos2unix
git ls-files '**.mk' | xargs dos2unix
git ls-files 'Makefile' | xargs dos2unix
git ls-files '**.clang*' | xargs dos2unix
git ls-files '**.gitignore' | xargs dos2unix
git ls-files '**.gitattributes' | xargs dos2unix
git ls-files 'CODEOWNERS' | xargs dos2unix

git ls-files '**.md' | xargs dos2unix
git ls-files '**.rst' | xargs dos2unix
git ls-files '**.txt' | xargs dos2unix
git ls-files 'LICENSE' | xargs dos2unix
git ls-files 'README' | xargs dos2unix

git ls-files '**.bvecs' | xargs dos2unix
git ls-files '**.bvals' | xargs dos2unix
git ls-files '**.fib' | xargs dos2unix
git ls-files '**.vtk' | xargs dos2unix
git ls-files '**.ffp' | xargs dos2unix

