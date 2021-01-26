from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from typing import NewType
from typing import Any
from typing import Dict
from typing import List

import psycopg2 # type: ignore
import os
import re

#vault_role_postgres_postgres_password: TaWJqCZHPFEEOb3lBX8M$
#vault_role_idempiere_db_adempiere_user_password: p3nR4qlqfc5Venz6AFHo$

class AnyClass:
    def __getattr__(self, item: str) -> Any:
        pass

DbConnection = NewType('DbConnection', AnyClass)

cFILE = 'module_utils/idempiere.py'

class Idempiere:
    cCLASS = 'Idempiere' 
    cMIGRATION_DIR = 'migration'

    def __init__(self, idempiereInstallationPath: str, dbAdempiereUserPassword: str, dbHost: str, dbPort = 5432):
        self.idempiereInstallationPath = idempiereInstallationPath
        self.dbAdempiereUserPassword = dbAdempiereUserPassword
        self.dbHost = dbHost
        self.dbPort = dbPort

    def getConnection(self) -> DbConnection:
        conn = psycopg2.connect(dbname='idempiere', user='adempiere', password = self.dbAdempiereUserPassword, host = self.dbHost, port = self.dbPort)
        return conn

    def getExecutedSqls(self) -> List[str]:
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute('select name from ad_migrationscript order by 1')
            result = cur.fetchall()
            result = list(map(lambda x: x[0], result))
            return result
        finally:
            con.close()
            cur.close()

    def getSourcodeSqlsDict(self, migrationDirPath: str) -> Dict[str, str]:
        sqls = {}
        for (dirpath, dirnames, filenames) in os.walk(migrationDirPath):
            if re.search(r'/i\d+.\d+/postgresql', dirpath) != None:
                fs = list(filter(lambda x: re.search(r'\.sql$', x) != None ,filenames))
                for f in fs:
                    sqls[f] = '{}/{}'.format(dirpath, f)
        return sqls

    def getNotExecutedSqlsList(self) -> List[str]:
        sourcecodeSqlsDict = self.getSourcodeSqlsDict('{}/{}'.format(self.idempiereInstallationPath, self.cMIGRATION_DIR)) 
        executedSqls = self.getExecutedSqls()

        sqlsNotExecutedDict = {}
        for sql in sourcecodeSqlsDict.keys():
            if sql not in set(executedSqls):
                sqlsNotExecutedDict[sql] = sourcecodeSqlsDict[sql]

        sqlsNotExecutedList = list(sqlsNotExecutedDict.keys());
        sqlsNotExecutedList.sort()
        return sqlsNotExecutedList

