#!/usr/bin/env bash

: ${PLAYBOOK:="$1"}
: ${PLAYBOOK:="hello-world"}

ansible-playbook -i localhost "playbook/${PLAYBOOK}/main.yml" --check --diff --connection=local