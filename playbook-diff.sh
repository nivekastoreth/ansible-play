#!/usr/bin/env bash

ansible-playbook -i localhost playbook/$1/main.yml --check --diff --connection=local