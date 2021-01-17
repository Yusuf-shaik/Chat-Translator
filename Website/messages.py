from connect import conn


def sendMessage(initialUser, destinationUser, text):
    sqlString = """insert into MSG.dbo.messages (fromUser, toUser, message, timestamp)
    values ('{}', '{}', '{}', getdate())""".format(initialUser, destinationUser, text)
    cursor = conn.cursor()
    cursor.execute(sqlString)
    conn.commit()
    cursor.close()
 

def getMessages():
    cursor = conn.cursor()
    sqlString = """select fromUser, message, timestamp, language
    from dbo.messages M
    left join dbo.languages L
    on M.toUser = L.[user]
    order by timestamp asc
    """
    cursor.execute(sqlString)
    records=cursor.fetchall()
    cursor.close()

    return records

# def initializeUser(user, language):
#     sqlString = """insert into dbo.languages
#     values ('{}', '{}')""".format(user, language)
#     cursor = conn.cursor()
#     cursor.execute(sqlString)
#     conn.commit()
#     cursor.close()

# def registered(user):
#     sqlString = "select case when exists (select user from dbo.languages where [user] = '{}') then 1 else 0 end".format(user)
#     cursor = conn.cursor()
#     cursor.execute(sqlString)
#     for row in cursor:
#         return row[0]
    


