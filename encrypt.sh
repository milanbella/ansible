set -x
find . -path './playbooks/*/group_vars/*/vault/*' -exec ansible-vault encrypt --vault-id=develop@~/ansible_valut_password {} \;
