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
    def __init__(self, dbAdempiereUserPassword: str, dbHost: str, dbPort = 5432):
        self.dbAdempiereUserPassword = dbAdempiereUserPassword
        self.dbHost = dbHost
        self.dbPort = dbPort

    def getConnection(self) -> DbConnection:
        cFUNC = 'getConnection()'
        try:
            conn = psycopg2.connect(dbname='idempiere', user='adempiere', password = self.dbAdempiereUserPassword, host = self.dbHost, port = self.dbPort)
            return conn
        except:
            raise Exception('{}:{}:{}: error'.format(self.cCLASS, cFILE, cFUNC))

    def getExecutedSqls(self) -> List[str]:
        cFUNC = 'getLisOfExecutedSqls()'
        try:
            con = self.getConnection()
            cur = con.cursor()
            cur.execute('select name from ad_migrationscript order by 1')
            result = cur.fetchall()
            result = list(map(lambda x: x[0], result))
            return result
        except:
            raise Exception('{}:{}:{}: error'.format(self.cCLASS, cFILE, cFUNC))
        finally:
            con.close()
            cur.close()

        def getSourcodeSqlsDict(migrationDirPath: str) -> Dict[str, str]:
            cFUNC = 'getLisOfSqls()'
            try:
                sqls = {}
                for (dirpath, dirnames, filenames) in os.walk(migrationDirPath):
                    if re.search(r'/i\d+.\d+/postgresql', dirpath) != None:
                        fs = list(filter(lambda x: re.search(r'\.sql$', x) != None ,filenames))
                        for f in fs:
                            sqls[f] = '{}/{}'.format(dirpath, f)
                return sqls
            except:
                raise Exception('{}:{}:{}: error'.format(self.cCLASS, cFILE, cFUNC))

        def getNotExecutedSqlsDict(sourcecodeSqlsDict: Dict[str, str], executedSqls: List[str]) -> Dict[str, str]:
            cFUNC = 'getNotExecutedSqlsDict()'
            try:
                sqls = {}
                executed = set(executedSqls);
                for sql in sourcecodeSqlsDict.keys():
                    if sql not in set(executedSqls):
                        sqls[sql] = sourcecodeSqlsDict[sql]
                return sqls
            except:
                raise Exception('{}:{}:{}: error'.format(self.cCLASS, cFILE, cFUNC))

