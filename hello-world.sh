#!/usr/bin/env bash

ansible-playbook -i localhost playbook/hello-world/main.yml --check --diff --connection=local