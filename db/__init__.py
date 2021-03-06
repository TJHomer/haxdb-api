import tables


class db:
    db = None
    tables = tables
    config = None
    logger = None

    def __init__(self, config, logger):
        self.config = config
        self.logger = logger

    def _TOBLOB(self, filedata):
        return self.db._TOBLOB(filedata)

    def _FROMBLOB(self, blobdata):
        return self.db._FROMBLOB(blobdata)

    def open(self):
        if self.config["TYPE"] == "SQLITE":
            import driver_sqlite
            self.db = driver_sqlite.db(self.config, self.logger)
        elif self.config["TYPE"] == "MARIADB":
            import driver_mariadb
            self.db = driver_mariadb.db(self.config, self.logger)

    def close(self):
        self.db.close()

    def create(self, tables, indexes):
        return self.db.create(tables, indexes)

    def query(self, sql, data=None, squelch=False):
        self.rowcount = None
        self.lastrowid = None
        self.error = None
        result = self.db.query(sql, data, squelch)
        self.rowcount = self.db.rowcount
        self.lastrowid = self.db.lastrowid
        self.error = self.db.error
        if int(self.config["DEBUG"]) == 1 and not squelch:
            sep = "##########################################################"
            sep += "#####################"
            self.logger.debug(sep)
            self.logger.debug("sql: {}".format(sql))
            self.logger.debug("data: {}".format(data))
            self.logger.debug("result: {}".format(result))
            self.logger.debug("rowcount: {}".format(self.rowcount))
            self.logger.debug("lastrowid: {}".format(self.lastrowid))
            self.logger.debug("error: {}".format(self.error))
            self.logger.debug(sep)

        return result

    def qaf(self, sql, data=None, squelch=False):
        self.query(sql, data, squelch=squelch)
        if self.error:
            return False
        return self.next()

    def next(self):
        return self.db.next()

    def commit(self):
        return self.db.commit()

    def rollback(self):
        return self.db.rollback()
