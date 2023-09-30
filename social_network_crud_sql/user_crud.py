# crud_operations.py
from database import cursor, conn

def create_user(username, email, bio=None):
    cursor.execute('''
        INSERT INTO users (username, email, bio)
        VALUES (?, ?, ?)
    ''', (username, email, bio))
    conn.commit()

def read_user(user_id=None):
    if user_id is not None:
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    else:
        cursor.execute('SELECT * FROM users')

    return cursor.fetchall()

def update_user(user_id, new_username=None, new_email=None, new_bio=None):
    update_data = {}
    if new_username:
        update_data['username'] = new_username
    if new_email:
        update_data['email'] = new_email
    if new_bio:
        update_data['bio'] = new_bio

    if update_data:
        set_query = ', '.join([f'{key} = ?' for key in update_data.keys()])
        cursor.execute(f'''
            UPDATE users
            SET {set_query}
            WHERE id = ?
        ''', (*update_data.values(), user_id))
        conn.commit()

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()

