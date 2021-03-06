#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

{ set -x; cd "${BASH_SOURCE[0]%/*/*/*}" || exit $?; { set +x; } 2>/dev/null; }
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1

name="$(python setup.py --name)" || exit
url="https://pypi.python.org/pypi/$name"
( set -x; open "$url" )
