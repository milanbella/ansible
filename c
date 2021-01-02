set -x
#ansible-playbook -i  hosts.yml   --vault-id=develop@~/ansible_valut_password playbooks/idempiere/idempiere_standalone_db.yml
ansible-playbook -i  hosts.yml   --vault-id=develop@~/ansible_valut_password playbooks/idempiere/idempiere_standalone_server.yml
