#!/bin/bash

version=$(poetry version --short)

printf "The current release version is $version.\n"
printf "Press [y/n] to proceed: "

read yn
case $yn in
    [Yy]* )
        git add --all
        git commit -v
        git tag $version
        git push --tags origin master;;
    * ) exit;;
esac
