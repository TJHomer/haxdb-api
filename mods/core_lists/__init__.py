import mod_db
import mod_api
import mod_tools
from mod_def import mod_def

db = None
config = None
haxdb = None
api = None


def init(app_haxdb, app_api, mod_config):
    global config, db, haxdb, api
    haxdb = app_haxdb
    config = mod_config
    db = haxdb.db
    api = app_api

    mod_db.init(db, config)
    mod_api.init(haxdb, api, config, mod_def)


def run():
    mod_db.run()
    mod_api.run()
