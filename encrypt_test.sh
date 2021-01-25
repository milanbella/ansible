set -x
find . -path './vars/test/vault/*' -exec ansible-vault encrypt --vault-id=test@~/ansible_valut_password_test {} \;
find . -path './playbooks/*/test/vault/*' -exec ansible-vault encrypt --vault-id=test@~/ansible_valut_password_test {} \;
find . -path './playbooks/test/vault/*' -exec ansible-vault encrypt --vault-id=test@~/ansible_valut_password_test {} \;

