#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import pymysql
from dbutils.pooled_db import PooledDB

from po.common.log import log
from po.core import get_conf


class DB:

    def __init__(self):
        self._pool = PooledDB(
            pymysql,
            host=get_conf.DB_HOST,
            port=get_conf.DB_PORT,
            user=get_conf.DB_USER,
            password=get_conf.DB_PASSWORD,
            database=get_conf.DB_DATABASE,
            charset=get_conf.DB_CHARSET,
            maxconnections=15,
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待
            autocommit=False  # 是否自动提交
        )
        self.conn = self._pool.connection()
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # type: ignore

    def close(self):
        """
        关闭数据库连接
        """
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, params=None):
        """
        执行sql语句

        :param sql: sql 语句
        :param params: 参数
        :return:
        """
        try:
            rowcount = self.cursor.execute(sql, params)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            log.error(f'❌ Execute sql error: {e}')
            raise e
        finally:
            self.close()
        return rowcount

    def execute_many(self, sql, params=None):
        """
        执行sql语句

        :param sql: sql 语句
        :param params: 参数
        :return:
        """
        try:
            rowcount = self.cursor.executemany(sql, params)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            log.error(f'❌ Execute sql error: {e}')
            raise e
        finally:
            self.close()
        return rowcount

    def fetchone(self, sql, params=None):
        """
        获取一条数据

        :param sql: sql 语句
        :param params: 参数
        :return:
        """
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
        except Exception as e:
            log.error(f'❌ Fetch one error: {e}')
            raise e
        finally:
            self.close()
        return result

    def fetchmany(self, sql, params=None, size=None):
        """
        获取多条数据

        :param sql: sql 语句
        :param params: 参数
        :param size: 获取的条数
        :return:
        """
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchmany(size)
        except Exception as e:
            log.error(f'❌ Fetch many error: {e}')
            raise e
        finally:
            self.close()
        return result

    def fetchall(self, sql, params=None):
        """
        获取所有数据

        :param sql: sql 语句
        :param params: 参数
        :return:
        """
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
        except Exception as e:
            log.error(f'❌ Fetch all error: {e}')
            raise e
        finally:
            self.close()
        return result


db = DB()
