import pymysql


def exec_sql_file(cursor, sql_file):
    """Script for execute sql file."""
    print("[INFO] Execution du script SQL: '%s'" % sql_file)
    statement = ""
    for line in open(sql_file):
        if line.strip().startswith('--'):   # ignore sql comment lines
            continue
        if not line.strip().endswith(';'):  # keep appending lines that don't end in ';'
            statement = statement + line
        else:   # when you get a line ending in ';' then exec statement and reset for next statement
            statement = statement + line
            # print "\n\n[DEBUG] Executing SQL statement:\n%s" % (statement)
            try:
                cursor.execute(statement)
            except pymysql.InternalError as e:
                print("[WARN] MySQLError during execute statement \n\tArgs: '%s'" % (str(e.args)))
            statement = ""
