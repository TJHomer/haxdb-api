import os, base64, json, time

api = None
db = None
config = None
tools = None

def init(app_api, app_db, app_config, mod_tools):
    global api, db, config, tools
    api = app_api
    db = app_db
    config = app_config
    tools = mod_tools


def run():
    @api.app.route("/RFID/asset", methods=["POST", "GET"])
    @api.app.route("/RFID/asset/<int:assets_id>/<rfid>", methods=["POST", "GET"])
    @api.require_auth
    @api.require_dba
    @api.no_readonly
    def mod_rfid_asset_auth(assets_id=None, rfid=None):
        assets_id = assets_id or api.data.get("assets_id")
        rfid = rfid or api.data.get("rfid")
        
        data = {}
        data["input"] = {}
        data["input"]["api"] = "RFID"
        data["input"]["action"] = "asset"
        data["input"]["assets_id"] = assets_id
        data["input"]["rfid"] = rfid
        
        sql = """
        SELECT 
        PFN.PEOPLE_COLUMN_VALUES_VALUE as PEOPLE_FIRST_NAME,
        PLN.PEOPLE_COLUMN_VALUES_VALUE as PEOPLE_LAST_NAME,
        A.ASSETS_NAME
        
        FROM PEOPLE P
        JOIN PEOPLE_COLUMNS PC 
        JOIN PEOPLE_COLUMN_VALUES PCV ON PCV.PEOPLE_COLUMN_VALUES_PEOPLE_COLUMNS_ID = PC.PEOPLE_COLUMNS_ID AND PCV.PEOPLE_COLUMN_VALUES_PEOPLE_ID = P.PEOPLE_ID
        JOIN ASSET_AUTHS AA ON AA.ASSET_AUTHS_PEOPLE_ID = P.PEOPLE_ID
        JOIN ASSETS A ON A.ASSETS_ID = AA.ASSET_AUTHS_ASSETS_ID
        LEFT OUTER JOIN PEOPLE_COLUMN_VALUES PFN ON PFN.PEOPLE_COLUMN_VALUES_PEOPLE_ID = PEOPLE_ID AND PFN.PEOPLE_COLUMN_VALUES_PEOPLE_COLUMNS_ID = (SELECT PEOPLE_COLUMNS_ID FROM PEOPLE_COLUMNS WHERE PEOPLE_COLUMNS_NAME='FIRST_NAME')
        LEFT OUTER JOIN PEOPLE_COLUMN_VALUES PLN ON PLN.PEOPLE_COLUMN_VALUES_PEOPLE_ID = PEOPLE_ID AND PLN.PEOPLE_COLUMN_VALUES_PEOPLE_COLUMNS_ID = (SELECT PEOPLE_COLUMNS_ID FROM PEOPLE_COLUMNS WHERE PEOPLE_COLUMNS_NAME='LAST_NAME')

        WHERE
        PC.PEOPLE_COLUMNS_NAME='RFID'
        AND PCV.PEOPLE_COLUMN_VALUES_VALUE = ?
        AND AA.ASSET_AUTHS_ASSETS_ID = ?
        """
        db.query(sql, (rfid,assets_id,))
        
        if db.error:
            return api.output(success=0, data=data, info=db.error)

        row = db.next()
        
        if row:
            data["row"] = dict(row)
            return api.output(success=1, data=data, info="ACCESS GRANTED")
        
        return api.output(success=0, info="PERMISSION DENIED", data=data)

