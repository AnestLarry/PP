from typing import Generator, Tuple, Any

import pyodbc


class DatabaseOperator(object):
    def __init__(self, driver: str, encoding: str = "utf-8"):
        self.conn: pyodbc.Connection = pyodbc.connect(driver)
        self.conn.setencoding(encoding=encoding)
        self.c: pyodbc.Cursor = self.conn.cursor()

    def select(self, tokens: str = "", fieldNames: str = "", tableNames: str = "", expressions: str = "", tail: str = "", params: Tuple = (),
               stmt: str = "select {tokens} {fieldNames} from {tableNames} where {expressions} {tail};") -> Generator[Tuple[Any]]:
        """
        execute select and return generator.

        stmt = stmt.format(tokens=tokens, fieldNames=fieldNames, tableNames=tableNames, expressions=expressions, tail=tail)

        :param tokens: such as DISTINCT, TOP
        :param fieldNames: such as NAME
        :param tableNames: such as PEOPLE
        :param expressions: such NAME = "John"
        :param tail: such as ORDER BY NAME
        :param params: add args to sql
        :param stmt: sql
        :return: a Generator of Tuple
        """
        stmt = stmt.format(tokens=tokens, fieldNames=fieldNames, tableNames=tableNames, expressions=expressions, tail=tail)
        self.c.execute(stmt, params=params)
        for i in self.c.fetchall():
            yield i

    def insert(self, tableNames: str = "", fieldNames: str = "", fieldValues: str = "", params: Tuple[str] = (),
               stmt: str = "insert into {tableName} {fieldNames} values ({fieldValues});") -> int:
        """
        insert values to table.

        stmt = stmt.format(fieldNames=fieldNames, fieldValues=fieldValues, tableNames=tableNames)

        :param tableNames: such as PEOPLE
        :param fieldNames: such as NAME
        :param fieldValues: such as ("John"),("Amy")
        :param params: add args to sql
        :param stmt: sql
        :return: A number of changes
        """
        stmt = stmt.format(fieldNames=fieldNames, fieldValues=fieldValues, tableNames=tableNames)
        self.c.execute(stmt, params=params)
        return self.c.rowcount

    def delete(self, tokens: str = "", tableNames: str = "", expressions: str = "", params: Tuple[str] = (),
               stmt: str = "delete {tokens} from {tableName} where {express};") -> int:
        """
        delete sets from table.

        stmt = stmt.format(tokens=tokens, tableNames=tableNames, expressions=expressions)

        :param tokens: such as DISTINCT, TOP
        :param tableNames: such as PEOPLE
        :param expressions: such NAME = "John"
        :param params: add args to sql
        :param stmt: sql
        :return: A number of changes
        """
        stmt = stmt.format(tokens=tokens, tableNames=tableNames, expressions=expressions)
        self.c.execute(stmt, params=params)
        return self.c.rowcount

    def update(self, tokens: str = "", tableNames: str = "", fieldAndValueSets: str = "", expressions: str = "", params: Tuple[str] = (),
               stmt: str = "update {tokens} {fieldAndValueSets} from {tableName} where {express};") -> int:
        """

        :param tokens: such as PEOPLE
        :param tableNames: such as PEOPLE
        :param fieldAndValueSets: such NAME = "John",AGE = 1
        :param expressions: such NAME = "John"
        :param params: add args to sql
        :param stmt: sql
        :return: A number of changes
        """
        stmt = stmt.format(tokens=tokens, fieldAndValueSets=fieldAndValueSets, tableNames=tableNames, expressions=expressions)
        self.c.execute(stmt, params=params)
        return self.c.rowcount

    def gc(self) -> None:
        self.c.close()
        self.c = None
        self.conn.close()
        self.conn = None

    def transaction_begin(self, token: str = "", name: str = "", stmt: str = "begin {token} {name};") -> None:
        """
        begin a transaction.

        :param token: such as trans (Non-essential)
        :param name: such as transformMoney (Non-essential)
        :param stmt: sql
        :return: None
        """
        stmt.format(token=token, name=name)
        self.c.execute(stmt)

    def transaction_commit(self, token: str = "", name: str = "", stmt: str = "commit {token} {name};") -> None:
        """
        commit a transaction.

        :param token: such as trans (Non-essential)
        :param name: such as transformMoney (Non-essential)
        :param stmt: sql
        :return: None
        """
        stmt.format(token=token, name=name)
        self.c.execute(stmt)

    def transaction_rollback(self, token: str = "", name: str = "", stmt: str = "rollback {token} {name};") -> None:
        """
        rollback a transaction.

        :param token: such as "to" (Non-essential)
        :param name: such as transformMoney (Non-essential)
        :param stmt: sql
        :return: None
        """
        stmt.format(token=token, name=name)
        self.c.execute(stmt)

    def execute_with_return(self, stmt: str = "", params: str = "") -> Generator[Tuple[Any]]:
        """
        :param stmt: sql
        :param params: add args to sql
        :return: a Generator of Tuple
        """
        self.c.execute(stmt, params)
        for i in self.c.fetchall():
            yield i

    def execute_without_return(self, stmt: str = "", params: str = "") -> int:
        """
        :param stmt: sql
        :param params: add args to sql
        :return: A number of changes
        """
        self.c.execute(stmt, params)
        return self.c.rowcount
