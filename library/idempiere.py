#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import psycopg2
import os
import re

#vault_role_postgres_postgres_password: TaWJqCZHPFEEOb3lBX8M$
#vault_role_idempiere_db_adempiere_user_password: p3nR4qlqfc5Venz6AFHo$

cFILE = 'migrate.py'


def getConnection():
    cFUNC = 'getConnection()'
    try:
        conn = psycopg2.connect(dbname='idempiere', user='adempiere', password='p3nR4qlqfc5Venz6AFHo', host='199.247.31.166')
        return conn
    except:
        raise Exception('{}:{}: error'.format(cFILE, cFUNC))

def getExecutedSqls():
    cFUNC = 'getLisOfExecutedSqls()'
    try:
        cur = getConnection().cursor()
        cur.execute('select name from ad_migrationscript order by 1')
        result = cur.fetchall()
        result = list(map(lambda x: x[0], result))
        return result
    except:
        raise Exception('{}:{}: error'.format(cFILE, cFUNC))

def getSourcodeSqlsDict(migrationDirPath):
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
        raise Exception('{}:{}: error'.format(cFILE, cFUNC))

def getNotExecutedSqlsDict(sourcecodeSqlsDict, executedSqls):
    cFUNC = 'getNotExecutedSqlsDict()'
    try:
        sqls = {}
        executed = set(executedSqls);
        for sql in sourcecodeSqlsDict.keys():
            if sql not in set(executedSqls):
                sqls[sql] = sourcecodeSqlsDict[sql]
        return sqls
    except:
        raise Exception('{}:{}: error'.format(cFILE, cFUNC))

def main():
    cFUNC = 'main()' 
    try:
        print('Hello world!')
        sourcecodeSqlsDict = getSourcodeSqlsDict('idempiere_migration')
        executedSqls = getExecutedSqls();
        sqlsDict = getNotExecutedSqlsDict(sourcecodeSqlsDict, executedSqls);
        print(sqlsDict)
    except:
        raise Exception('{}:{}: error'.format(cFILE, cFUNC))

