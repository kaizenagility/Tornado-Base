import logging
import pymongo
import settings

class Proxy(object):
  _db = None
  def __getattr__(self, name):
    if Proxy._db == None:
      mongo_database = settings.get('mongo_database')
      logging.info("connecting to mongo at %s:%d/%s" % (mongo_database['host'], mongo_database['port'], mongo_database['db']))
      connection = pymongo.MongoClient(
        'mongodb://%s:%s/%s' % (mongo_database['host'],mongo_database['port'],mongo_database['db']),
        connectTimeoutMS=5000
      )
      Proxy._db = connection[mongo_database['db']]

    return getattr(self._db, name)

db = Proxy()