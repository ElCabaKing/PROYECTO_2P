from src.config.db import db_pool
from psycopg2.extras import RealDictCursor

class AuthModel():
    def get_user_by_cid(self, log_in_Data):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                        SELECT * FROM tb_user
                        WHERE cedula = %s;
                        """,(
                            log_in_Data['Cedula'],))
                user_data = cur.fetchone()
                cur.close()
                db_pool.putconn(conn)
        return user_data
    
    def get_user_by_id(self, id):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                        SELECT id,correo FROM tb_user
                        WHERE id = %s;
                        """,(
                            id,))
                user_data = cur.fetchone()
                cur.close()
                db_pool.putconn(conn)
        return user_data
    
    def get_user_by_email(self, email):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                                select id, nombre, apellido from tb_user tu 
                                where tu.correo = %s;
                                """,(
                                    email,
                                    ))
                user= cur.fetchone(
                                )
        return user
    
    def save_recovery_token(self, email, token):
        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                        INSERT INTO tb_recovery_tokens
                        (user_email, recovery_token)
                        VALUES (%s, %s);
                    """, (
                        email,
                        token
                    ))
                conn.commit()
                cur.close()
                db_pool.putconn(conn)
        return None
    
    def update_user_password(self, user_id, new_password):
        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                        UPDATE tb_user
                        SET contrasenahash = %s
                        WHERE id = %s;
                    """, (
                        new_password,
                        user_id
                    ))
                conn.commit()
                cur.close()
                db_pool.putconn(conn)
        return None