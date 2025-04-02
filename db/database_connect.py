import psycopg2
from config.config import HOST, USER, PASSWORD, DB_NAME

from aiogram.types import Message

class Database():
    def __init__(self):
        self.cnxn = psycopg2.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DB_NAME
        )
        self.cursor = self.cnxn.cursor()


    async def add_user(self, msg: Message) -> None:
        sql = """
            INSERT INTO users
            (id, username, first_name, last_name) VALUES
            (%s, %s, %s, %s)
        """
        try:
            self.cursor.execute(sql, (msg.from_user.id, msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, ))
        except Exception as e:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def user_exists(self, user_id: int) -> bool:
        sql = """
            SELECT COUNT(*) FROM users
            WHERE id = %s
        """

        self.cursor.execute(sql, (user_id, ))
        exists = self.cursor.fetchone()

        return True if exists[0] == 1 else False
    

    async def get_content(self, content_id: int) -> str | tuple:
        sql = """
            SELECT content FROM contents WHERE id = %s
        """

        self.cursor.execute(sql, (content_id, ))
        content = self.cursor.fetchone()

        return content[0]
        

    async def user_is_active(self, user_id: int) -> bool:
        sql = """
            SELECT is_active FROM users
            WHERE id = %s
        """

        self.cursor.execute(sql, (user_id, ))
        is_active = self.cursor.fetchone()

        return True if is_active[0] == '1' else False
    

    async def make_user_active(self, user_id: int) -> None:
        sql = """
            UPDATE users SET is_active = '1'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id, ))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def make_user_inactive(self, user_id: int) -> None:
        sql = """
            UPDATE users SET is_active = '0'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id, ))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def start_get_notifications(self, user_id: int) -> None:
        sql = """
            UPDATE users SET get_notifications = '1'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id, ))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def stop_get_notifications(self, user_id: int) -> None:
        sql = """
            UPDATE users SET get_notifications = '0'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id, ))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def is_get_notifications(self, user_id: int) -> bool:
        sql = """
            SELECT get_notifications FROM users
            WHERE id = %s
        """

        self.cursor.execute(sql, (user_id, ))
        is_get_notifications = self.cursor.fetchone()

        return True if is_get_notifications[0] == '1' else False
    

    async def get_active_users(self) -> list:
        sql = """
            SELECT id FROM users
            WHERE is_active = '1' AND get_notifications = '1' 
        """

        self.cursor.execute(sql)
        users = self.cursor.fetchall()

        return users
    

    async def set_yes_dinner(self, user_id: int) -> None:
        sql = """
            UPDATE users SET yes_dinner = '1'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id,))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def set_no_dinner(self, user_id: int) -> None:
        sql = """
            UPDATE users SET yes_dinner = '0'
            WHERE id = %s
        """

        try:
            self.cursor.execute(sql, (user_id,))
        except Exception:
            self.cnxn.rollback()
        finally:
            self.cnxn.commit()


    async def is_yes_dinner(self, user_id: int) -> bool:
        sql = """
            SELECT yes_dinner FROM users
            WHERE id = %s
        """

        self.cursor.execute(sql, (user_id,))
        yes_dinner = self.cursor.fetchone()

        return True if yes_dinner[0] == '1' else False