from src.config.db import db_pool
from psycopg2.extras import RealDictCursor

class UserModel():

    def insert_new_user(self, user):
        print(user)
        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO tb_user
                    (cedula, nombre, apellido, correo, contrasena_hash, role_id, sucursal_id, restaurant_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    user['cedula'],
                    user['nombre'],
                    user['apellido'],
                    user['correo'],
                    user['contrasena'].decode("utf-8"),
                    user['role_id'],
                    user['sucursal_id'],
                    user['restaurant_id'],
                ))
                conn.commit()
                cur.close()
                db_pool.putconn(conn)
        return True


    def get_user_list(self, num_offset, sucursal_id):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                           select tu.nombre , tu.apellido , tu.correo ,tu.activo, tu.cedula, tu.role_id from tb_user tu 
                            where tu.sucursalid = %s
                            order by tu.id 
                            limit 10 offset %s;
                            """,(
                                sucursal_id,
                                num_offset,
                                ))
                users= cur.fetchall()
        return users
    
    
    def get_user_list_restaurant(self, num_offset, restauran_id):
                with db_pool.getconn() as conn:
                    with conn.cursor(cursor_factory=RealDictCursor) as cur:
                        cur.execute("""
                                select tu.nombre , tu.apellido , tu.correo ,tu.activo, tu.cedula, tu.role_id from tb_user tu 
                                    where tu.restaurant_id = %s
                                    order by tu.id 
                                    limit 10 offset %s;
                                    """,(
                                        restauran_id,
                                        num_offset,
                                        ))
                        users= cur.fetchall()
                return users
    
    def get_user_by_id(self, user_id):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, cedula, nombre, apellido, correo, role_id, sucursal_id, restaurant_id, activo
                    FROM tb_user
                    WHERE id = %s;
                """, (user_id,))
                user = cur.fetchone()
                cur.close()
                db_pool.putconn(conn)
        return user

    def update_user(self, user_id, update_data):
        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                set_clause = []
                params = []
                
                for key, value in update_data.items():
                    if key in ['nombre', 'apellido', 'correo', 'role_id', 'sucursal_id']:
                        set_clause.append(f"{key} = %s")
                        params.append(value)
                
                if not set_clause:
                    return False
                
                params.append(user_id)
                
                query = f"""
                    UPDATE tb_user
                    SET {', '.join(set_clause)}
                    WHERE id = %s;
                """
                
                cur.execute(query, tuple(params))
                conn.commit()
                cur.close()
                db_pool.putconn(conn)
        
        return True
    
    def get_all_roles(self):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, nombre FROM tb_roles
                    ORDER BY id;
                """)
                roles = cur.fetchall()
                cur.close()
                db_pool.putconn(conn)
        return roles
        return True
    

