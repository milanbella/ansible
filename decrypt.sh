set -x
ansible-vault decrypt --vault-id develop@~/ansible_valut_password playbooks/test/roles/group_vars/postgres/vault/main.yml
ansible-vault decrypt --vault-id develop@~/ansible_valut_password playbooks/idempiere/group_vars/idempiere/vault/main.yml
ansible-vault decrypt --vault-id develop@~/ansible_valut_password playbooks/idempiere/group_vars/idempiere_db/vault/main.yml
