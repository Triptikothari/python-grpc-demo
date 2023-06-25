from django_redis import get_redis_connection
import json


class RedisAccessor(object):

    @staticmethod
    def setData(key, value, connection='default', timeout=None):
        try:
            con = get_redis_connection(connection)
            data = json.dumps(value, default=str)
            con.set(key, data, timeout)
        except Exception as e:
            print(str(e))

    @staticmethod
    def setStringData(key, value, connection='default', timeout=None):
        try:
            con = get_redis_connection(connection)
            con.set(key, value, timeout)
        except Exception as e:
            print(str(e))

    @staticmethod
    def getData(key, connection='default'):
        try:
            con = get_redis_connection(connection)
            value = json.loads(con.get(key))
            return value
        except Exception as e:
            print(str(e))

    @staticmethod
    def getStringData(key, connection='default'):
        try:
            con = get_redis_connection(connection)
            return con.get(key)
        except Exception as e:
            print(str(e))

    @staticmethod
    def flushAll(connection='default'):
        try:
            get_redis_connection(connection).flushall()
            return True
        except Exception as e:
            print(str(e))
            return False

    @staticmethod
    def checkKey(value, connection='default'):
        try:
            con = get_redis_connection(connection)
            isPresent = con.exists(value)
            return isPresent
        except Exception as e:
            return 0

    @staticmethod
    def matchKey(value, connection='default'):
        try:
            con = get_redis_connection(connection)
            key = con.scan(value + "*")
            return key[0]
        except Exception as e:
            print(str(e))
            return 0

    @staticmethod
    def deleteKey(key, connection='default'):
        try:
            con = get_redis_connection(connection)
            isDeleted = con.delete(key)
            return isDeleted
        except Exception as e:
            print(e)
            return 0
