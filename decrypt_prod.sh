set -x
find . -path './vars/prod/vault/*' -exec ansible-vault decrypt --vault-id=prod@~/ansible_valut_password_prod {} \;
find . -path './playbooks/*/prod/vault/*' -exec ansible-vault decrypt --vault-id=prod@~/ansible_valut_password_prod {} \;
find . -path './playbooks/prod/vault/*' -exec ansible-vault decrypt --vault-id=prod@~/ansible_valut_password_prod {} \;

