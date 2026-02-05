from src.config.db import db_pool
from psycopg2.extras import RealDictCursor

class AuthModel():
    def get_user_by_cid(self, login_Data):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                        SELECT * FROM usuarios
                        WHERE cedula = %s;
                        """,(
                            login_Data['cedula'],))
                user_data = cur.fetchone()
                print(user_data)
            return user_data
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_user_by_id(self, id):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                        SELECT id,correo FROM usuarios
                        WHERE id = %s;
                        """,(
                            id,))
                user_data = cur.fetchone()
            return user_data
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_user_by_email(self, email):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                                select id, nombre, apellido from usuarios tu 
                                where tu.correo = %s;
                                """,(
                                    email,
                                    ))
                user= cur.fetchone()
            return user
        finally:
            cur.close()
            db_pool.putconn(conn)

    def update_user_password(self, user_id, new_password):
        conn = db_pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                        UPDATE usuarios
                        SET contrasena_hash = %s
                        WHERE id = %s;
                    """, (
                        new_password,
                        user_id
                    ))
                conn.commit()
            return None
        finally:
            cur.close()
            db_pool.putconn(conn)