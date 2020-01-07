## Usage


```bash
# Get the history file
$ history > history.txt

# Install
$ pip install shell_history_analysis

# You have to know which shell you have
# This is important, because the `history` command has different outputs in
# different shells.
# Fish shell has only the command itself as an output.
$ python analyze.py history.txt --shell bash
```

![History of Commands](https://raw.githubusercontent.com/MartinThoma/shell-history-analysis/master/docs/history.png)


## Grouping and Anonymization

You can provide a `grouping.yaml` file to group commands together. The default
is the following:

```bash
'CLI Programs':
  - aspell
  - ffmpeg
  - ffprobe
  - dot
  - neato
  - fdp
  - circo
  - convert
  - md5sum
  - curl
  - wget
  - jq
  - netstat
'CLI Utils':
  - mv
  - cd
  - ..
  - ...
  - ls
  - rm
  - grep
  - cat
  - cp
  - mkdir
  - head
  - tail
  - chmod
  - chown
  - watch
  - open
  - xdg-open
  - file
  - history
  - tree
  - touch
  - find
  - locate
  - ping
  - man
  - ln
  - wc
  - df
  - du
  - pwd
  - ll
Databases:
  - mysql
  - psql
Dev-Tools:
  - make
  - meld
  - diff
  - cookiecutter
  - cloc
Docker:
  - docker
  - docker-compose
Editor(s):
  - sublime
  - subl
  - vim
  - vi
  - spyder
  - spyder3
  - nano
Java:
  - mvn
  - java
  - javac
JS:
  - npm
  - node
  - ntl
  - yarn
  - nvm
  - lerna
Cloud:
  - az
  - aws
LaTeX:
  - pdflatex
  - tlmgr
Python:
  - python
  - python2
  - python3
  - pip
  - pip2
  - pip3
  - virtualenv
  - venv
  - black
  - isort
  - pylint
  - mypy
  - pytest
  - flask
  - pyenv
  - coverage
  - tox
  - flake8
  - twine
  - pydocstyle
  - pip-compile
  - pylama
  - pybabel
  - pep8
  - piprot
  - jupyter
  - alembic
Remote:
  - scp
  - ssh
  - ssh-keygen
Rust:
  - cargo
'Shell Scripting':
  - for
  - date
'System Management':
  - kill
  - killall
  - echo
  - export
  - env
  - ps
  - top
  - htop
  - atop
  - systemctl
  - sysctl
  - ip
  - ifconfig
  - which
  - sysbench
  - service
  - dmesg
'System Package Manager':
  - apt
  - apt-get
  - apt-cache
  - update-alternatives
  - dpkg
  - add-apt-repository
  - brew
  - mas
'Web Development':
  - ab
  - http
  - ng
git:
  - git
  - git-fame
```
