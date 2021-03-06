mod_def = {}

mod_def["PEOPLE_RFID"] = {
    "NAME": "PEOPLE_RFID",
    "TABLE": "PEOPLE_RFID",
    "ROWID": "PEOPLE_RFID_ID",
    "CONTEXT_ROW": "PEOPLE_RFID_PEOPLE_ID",
    "COLS": [
        {
         "CATEGORY": "ROW",
         "NAME": "PEOPLE_RFID_ID",
         "HEADER": "ID",
         "TYPE": "INT",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 0,
         "NEW": 0,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "PEOPLE_RFID_INSERTED",
         "HEADER": "CREATED",
         "TYPE": "STR",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "CATEGORY": "PERSON RFID",
         "NAME": "PEOPLE_RFID_NAME",
         "HEADER": "NAME",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 1,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "CATEGORY": "PERSON RFID",
         "NAME": "PEOPLE_RFID_PEOPLE_ID",
         "HEADER": "OWNER",
         "TYPE": "ID",
         "ID_API": "PEOPLE",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "CATEGORY": "PERSON RFID",
         "NAME": "PEOPLE_RFID_RFID",
         "HEADER": "RFID",
         "TYPE": "ASCII",
         "SIZE": 255,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "CATEGORY": "PERSON RFID",
         "NAME": "PEOPLE_RFID_ENABLED",
         "HEADER": "ENABLED",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
         "DEFAULT_VALUE": 0,
        },
    ],
    "ORDER": ["PEOPLE_RFID_NAME"]
}
