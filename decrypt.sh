set -x
ansible-vault decrypt --vault-id develop@~/ansible_valut_password playbooks/test/roles/group_vars/postgres/vault/main.yml
