#!/usr/bin/env bash

: ${PLAYBOOK:="hello-world"}

ansible-playbook -i localhost "playbook/${PLAYBOOK}/main.yml" --check --diff --connection=local "$@"