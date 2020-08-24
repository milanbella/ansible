set -x
ansible-vault encrypt --vault-id develop@~/ansible_valut_password playbooks/test/roles/group_vars/postgres/vault/main.yml
