mod_def = {}

mod_def["UDF"] = {
    "NAME": "UDF",
    "TABLE": "UDF",
    "ROWID": "UDF_ID",
    "UDF": False,
    "CONTEXT_ROW": None,
    "COLS": [
        {
         "CATEGORY": "ROW",
         "NAME": "UDF_ID",
         "HEADER": "ID",
         "TYPE": "INT",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "NEW": 0,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "UDF_CONTEXT",
         "HEADER": "CONTEXT",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "UDF_CONTEXT_ID",
         "HEADER": "CONTEXT_ID",
         "TYPE": "INT",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "UDF_INSERTED",
         "HEADER": "CREATED",
         "TYPE": "STR",
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
        },
        {
         "CATEGORY": "ROW",
         "NAME": "UDF_INTERNAL",
         "HEADER": "INTERNAL",
         "TYPE": "BOOL",
         "EDIT": 0,
         "QUERY": 0,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 1,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_CATEGORY",
         "HEADER": "CATEGORY",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_NAME",
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
         "CATEGORY": "UDF",
         "NAME": "UDF_TYPE",
         "HEADER": "TYPE",
         "TYPE": "SELECT",
         "OPTIONS": ["TEXT", "INT", "FLOAT", "BOOL", "LIST",
                     "ID", "FILE", "DATE", "TIMESTAMP"],
         "SIZE": 50,
         "EDIT": 0,
         "QUERY": 1,
         "SEARCH": 1,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_LISTS_ID",
         "HEADER": "LIST",
         "TYPE": "ID",
         "ID_API": "LISTS",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_API",
         "HEADER": "API",
         "TYPE": "STR",
         "SIZE": 50,
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_ORDER",
         "HEADER": "ORDER",
         "TYPE": "FLOAT",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
         "DEFAULT_VALUE": 999,
        },
        {
         "CATEGORY": "UDF",
         "NAME": "UDF_ENABLED",
         "HEADER": "ENABLED",
         "TYPE": "BOOL",
         "EDIT": 1,
         "QUERY": 1,
         "SEARCH": 0,
         "REQUIRED": 0,
         "INTERNAL": 0,
         "DEFAULT": 1,
         "NEW": 1,
        },
    ],
    "ORDER": ["UDF_ORDER", "UDF_NAME"]
}
