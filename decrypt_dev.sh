set -x
find . -path './playbooks/*/dev/vault/*' -exec ansible-vault decrypt --vault-id=develop@~/ansible_valut_password {} \;
find . -path './playbooks/*/group_vars/dev_*/vault/*' -exec ansible-vault decrypt --vault-id=develop@~/ansible_valut_password {} \;

