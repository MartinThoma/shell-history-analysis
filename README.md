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
$ shell_history_analysis history.txt --shell=zsh
Assumed shell: zsh
Grouping filepath: /home/moose/GitHub/shell-history-analysis/shell_history_analysis/grouping.yaml

CLI Utils                 2731
git                       2498
Python                    1536
Editor(s)                  905
System Package Manager     271
Dev-Tools                  203
Docker                     187
System Management          160
mutmut                     153
CLI Programs                88
pipenv                      53
clana                       43
conda                       36
exercism                    33
7z                          21
hwrt                        21
Shell Scripting             21
pandoc                      21
gzip                        20
Name: base_command, dtype: int64
Writing image to /home/moose/history.png
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
