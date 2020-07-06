__author__ = '10639'
from sshtunnel import SSHTunnelForwarder
import pymysql

server = SSHTunnelForwarder(
        ('sshhost.domain.com', 22),  # B机器的配置
        ssh_password='ssh_password',
        ssh_username='ssh_username',
        remote_bind_address=('mysqlhost.domain.com', pymysql.port)
)
server.start()

self.client = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                              port=server.local_bind_port,
                              user='username',
                              passwd='password',
                              db='dbname')
