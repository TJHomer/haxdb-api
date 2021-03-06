import os
import sys
from ConfigParser import ConfigParser
from os.path import join, isfile
import glob

mods = {}
config = None
haxdb = None
db = None


def read_mod_config(config_file):
    config = {
        "MOD": {
            "ENABLED": 1,
        }
    }
    print config_file,
    if isfile(config_file):
        print "FOUND"
        cfg = ConfigParser()
        cfg.read(config_file)
        for section in cfg.sections():
            config[section] = {}
            for option in cfg.options(section):
                config[section.upper()][option.upper()] = cfg.get(section,
                                                                  option)
    else:
        print "NO"
    return config


def init(hdb, app_api):
    global config, haxdb, db, api
    haxdb = hdb
    config = haxdb.config
    db = haxdb.db
    api = app_api


def run():
    global mods, config, haxdb, db
    sys.path.insert(0, config["MOD"]["PATH"])
    mod_names = []

    core_pattern = "{}/core_*".format(config["MOD"]["PATH"])
    for name in glob.glob(core_pattern):
        mod_names.append(os.path.basename(name))

    core_pattern = "{}/user_*".format(config["MOD"]["PATH"])
    for name in glob.glob(core_pattern):
        mod_names.append(os.path.basename(name))

    db.open()

    for mod_name in mod_names:
        mod_config_file = os.path.join(config["MOD"]["PATH"],
                                       mod_name,
                                       "mod.cfg")
        mod_config = read_mod_config(mod_config_file)
        if int(mod_config["MOD"]["ENABLED"]) == 1:
            haxdb.logger.info("{}.init()".format(mod_name))
            mod = __import__(mod_name)
            mod.init(haxdb, api, mod_config)
            mods[mod_name] = mod
        else:
            haxdb.logger.info("{} DISABLED".format(mod_name))

    print ""

    for mod in mods:
        haxdb.logger.info("{}.run()".format(mod))
        mods[mod].run()
    print ""

    db.close()
