import sqlite3

DB_PATH = './socialmedia.db'
NOTSTARTED = 'Not Started'
INPROGRESS = 'In Progress'
COMPLETED = 'Completed'


def add_to_user(username):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into users(username) VALUES(?)', [ username])
        conn.commit()
        return {"id": c.lastrowid, "username": username}
    except Exception as e:
        print('Error: ', e)
        return None


def add_to_post(text, user_id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('insert into posts(text, user_id) VALUES(?, ?)', [text, user_id])
        conn.commit()
        return {"id": c.lastrowid, "text": text, "user_id": user_id}
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_posts():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from posts')
        rows = c.fetchall()
        return { "count": len(rows), "posts": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_all_users():
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('select * from users')
        rows = c.fetchall()
        return { "count": len(rows), "users": rows }
    except Exception as e:
        print('Error: ', e)
        return None

def get_post(text):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute("select text from posts where id=%s" % text)
        text = c.fetchone()[0]
        print(text)
        return text
    except Exception as e:
        print('Error: ', e)
        return None
    
def update_post(id, text):  
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('update posts set text=? where id=?', (text, id))
        conn.commit()
        return {"id": id, "text": text}
    except Exception as e:
        print('Error: ', e)
        return None


def delete_post(id):
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('delete from posts where id=?', (id,))
        conn.commit()
        return {'id': id}
    except Exception as e:
        print('Error: ', e)
        return None