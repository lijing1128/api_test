# -*- coding: utf-8 -*-
# @Time    : 2020/6/10 10:45
# @Author  : wangy
# @File    : configDb.py

import pymysql
import readConfig
from config import logging
from sshtunnel import SSHTunnelForwarder



class MyDB:
    global config,ssh_host,ssh_port,ssh_password,ssh_username,remote_bind_address,remote_bind_port,mysql_username,mysql_password
    host = readConfig.localReadConfig.get_db("host")
    username = readConfig.localReadConfig.get_db("username")
    password = readConfig.localReadConfig.get_db("password")
    port = readConfig.localReadConfig.get_db("port")
    database = readConfig.localReadConfig.get_db("database")
    config = {
        'host': str(host),
        'user': username,
        'passwd': password,
        'port': int(port)
    }
    ssh_host = str(readConfig.localReadConfig.get_db_ssh("ssh-host"))
    ssh_port = int(readConfig.localReadConfig.get_db_ssh("ssh-port"))
    ssh_password = readConfig.localReadConfig.get_db_ssh("ssh-password")
    ssh_username = readConfig.localReadConfig.get_db_ssh("ssh-username")
    remote_bind_address = str(readConfig.localReadConfig.get_db_ssh("remote-bind-address"))
    remote_bind_port = int(readConfig.localReadConfig.get_db_ssh("remote-bind-port"))
    mysql_username = readConfig.localReadConfig.get_db_ssh("mysql-username")
    mysql_password = readConfig.localReadConfig.get_db_ssh("mysql-password")



    def __init__(self):
        self.db = None
        self.cursor = None

    def connectDB(self):
        try:
            # connect to DB
            self.db = pymysql.connect(**config)
            # create cursor
            self.cursor = self.db.cursor()
            log.logger.logger.info("Connect DB successfully!")
        except ConnectionError as ex:
            log.logger.logger.error(str(ex))

    def executeSQL(self, sql, params=None):
        self.connectDB()
        # executing sql
        try:
            self.cursor.execute(sql, params)
            # executing by committing to DB
            self.db.commit()
        except Exception:
            log.logger.logger.error("sql错误")
            self.closeDB()
        return self.cursor

    def connectDB_b(self):

        self.server = SSHTunnelForwarder(
                (ssh_host, ssh_port),  # B机器的配置
                ssh_password=ssh_password,
                ssh_username=ssh_username,
                remote_bind_address=(remote_bind_address, remote_bind_port))
        self.server.start()
        try:
            # connect to DB
            self.db = pymysql.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                                 port=self.server.local_bind_port,
                                 user=mysql_username,
                                 passwd=mysql_password
                                 )
            # create cursor
            self.cursor = self.db.cursor()
            log.logger.logger.info("Connect DB successfully!")
        except ConnectionError as ex:
            log.logger.logger.error(str(ex))

    def executeSQL_b(self, sql, params=None):
        self.connectDB_b()
        # executing sql
        try:
            self.cursor.execute(sql, params)
            # executing by committing to DB
            self.db.commit()
        except Exception:
            log.logger.logger.error("sql错误")
            self.closeDB()
            self.server.close()
        return self.cursor


    def get_all(self, cursor):
        value = cursor.fetchall()
        return value

    def get_one(self, cursor):
        value = cursor.fetchone()
        return value

    def closeDB(self):
        self.db.close()
        log.logger.logger.info("Database closed!")


if __name__ == '__main__':
    MyDB = MyDB()
    MyDB.connectDB_b()
    MyDB.closeDB()
    MyDB.server.close()