import sqlite3

class Database():
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor= self.connection.cursor()
    
    def user_exist(self, user_id, table=None):#work
        with self.connection:
            if table == 'users':
                result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?",(user_id, )).fetchall()
            else:
                result = self.cursor.execute("SELECT * FROM `sliv_info` WHERE `user_id` = ?",(user_id, )).fetchall()
            return bool(len(result))
    
    def add_user(self, user_id, user_name):#work
        with self.connection:
            return self.cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, user_name, ))
    
    def get_users_id(self):
        with self.connection:
            return self.cursor.execute("SELECT user_id FROM users").fetchall()
    
    def edit_status(self, user_id):#work
        with self.connection:
            return self.cursor.execute("UPDATE sliv_info SET status='payment' WHERE user_id= ?", (user_id, ))
    
    def addIn_sliv(self, info):#work
        with self.connection:
            return self.cursor.execute("""
            INSERT INTO
                sliv_info
                (
                    user_id,
                    link, 
                    status
                )
            VALUES (?, ?, ?)""",
            (
                info['user_id'],
                info['link'],
                "not payment"
            ))    
    
    def edit_sliv(self, info):#work
        with self.connection:
            return self.cursor.execute("""
                    UPDATE sliv_info
                    SET
                    link= ?
                    WHERE user_id= ?""", 
                ( 
                info['link'],
                info['user_id'],))
            
    def select_sliv(self, status=None):#work
        with self.connection:
            if status:
                return self.cursor.execute("SELECT * FROM sliv_info WHERE status = ?", (status,)).fetchall()
               
    def exist_name(self, user_id, username):#work
        with self.connection:   
            result= self.cursor.execute("SELECT username FROM users WHERE user_id= ?", ( user_id,)).fetchone()
            if result[0] == None:
                return self.cursor.execute("UPDATE users SET username = ? WHERE user_id = ?", (username, user_id,))
            else:
                pass
            
    def get_link(self):
        with self.connection:
            return self.cursor.execute("SELECT link FROM links").fetchone()[0]
        
    def set_link(self, referance):
        with self.connection:
            return self.cursor.execute("UPDATE links SET link = ?", (referance,))