import asyncio


class Cursor:
    def __init__(self, impl, connection):
        self._conn = connection
        self._impl = impl
        self._loop = connection.loop

    def close(self):
        fut = self._conn._execute(self._impl.close)
        return fut

    @property
    def connection(self):
        return self._conn

    @property
    def rowcount(self):
        return self._conn

    @property
    def description(self):
        return self._conn.description

    @property
    def closed(self):
        return self._impl.closed

    @property
    def arraysize(self):
        return self._conn.arraysize

    @arraysize.setter
    def arraysize(self, size):
        self._conn.arraysize = size

    def execute(self, sql, *params):
        fut = self._conn._execute(self._impl.execute, sql, *params)
        return fut

    def executemany(self, sql, *params):
        fut = self._conn._execute(self._impl.executemany, sql, *params)
        return fut

    @asyncio.coroutine
    def setinputsizes(self, *args, **kwargs):
        return None

    @asyncio.coroutine
    def setoutputsize(self, *args, **kwargs):
        return None

    def fetchone(self):
        fut = self._conn._execute(self._impl.fetchone)
        return fut

    def fetchall(self):
        fut = self._conn._execute(self._impl.fetchall)
        return fut

    def fetchmany(self, size):
        fut = self._conn._execute(self._impl.fetchmany, size)
        return fut

    def nextset(self):
        fut = self._conn._execute(self._impl.nextset)
        return fut

    def tables(self, table=None, catalog=None, schema=None, tableType=None):
        fut = self._conn._execute(self._impl.tables, table=table,
                                  catalog=catalog, schema=schema,
                                  tableType=tableType)
        return fut

    def columns(self, table=None, catalog=None, schema=None, column=None):
        fut = self._conn._execute(self._impl.columns, table=table,
                                  catalog=catalog, schema=schema,
                                  column=column)
        return fut

    @asyncio.coroutine
    def statistics(self, catalog=None, schema=None, unique=False, quick=True):
        fut = self._conn._execute(self._impl.statistics, catalog=catalog,
                                  schema=schema, unique=unique, quick=quick)
        return fut

    def rowIdColumns(self, table, catalog=None, schema=None, nullable=True):
        fut = self._conn._execute(self._impl.rowIdColumns, table,
                                  catalog=catalog, schema=schema,
                                  nullable=nullable)
        return fut

    def rowVerColumns(self, table, catalog=None, schema=None, nullable=True):
        fut = self._conn._execute(self._impl.rowVerColumns, table,
                                  catalog=catalog, schema=schema,
                                  nullable=nullable)
        return fut

    def primaryKeys(self, table, catalog=None, schema=None):
        fut = self._conn._execute(self._impl.primaryKeys, table,
                                  catalog=catalog, schema=schema)
        return fut

    # TODO: check source code of pyodbc regadring table argument
    def foreignKeys(self, table=None, catalog=None, schema=None,
                    foreignTable=None, foreignCatalog=None,
                    foreignSchema=None):
        fut = self._conn._execute(self._impl.foreignKeys, table=table,
                                  catalog=catalog, schema=schema,
                                  foreignTable=foreignTable,
                                  foreignCatalog=foreignCatalog,
                                  foreignSchema=foreignSchema)
        return fut

    def getTypeInfo(self, sqlType=None):
        fut = self._conn._execute(self._impl.getTypeInfo, sqlType)
        return fut

    def procedures(self, procedure=None, catalog=None, schema=None):
        fut = self._conn._execute(self._impl.procedures, procedure=procedure,
                                  catalog=catalog, schema=schema)
        return fut

    def procedureColumns(self, procedure=None, catalog=None, schema=None):
        fut = self._conn._execute(self._impl.procedureColumns,
                                  procedure=procedure, catalog=catalog,
                                  schema=schema)
        return fut

    def skip(self, count):
        fut = self._conn._execute(self._impl.skip, count)
        return fut

    def commit(self):
        fut = self._conn._execute(self._impl.commit)
        return fut

    def rollback(self):
        fut = self._conn._execute(self._impl.rollback)
        return fut