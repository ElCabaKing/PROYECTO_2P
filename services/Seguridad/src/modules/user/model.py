from src.config.db import db_pool
from psycopg2.extras import RealDictCursor

class UserModel():

    def insert_new_user(self, user):
        print(user)
        with db_pool.getconn() as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO tb_user
                    (cedula, nombre, apellido, correo, contrasenahash, roleid, sucursalid)
                    VALUES (%s, %s, %s, %s, %s, %s, %s);
                """, (
                    user['Cedula'],
                    user['Nombre'],
                    user['Apellido'],
                    user['Correo'],
                    user['Contrasena'].decode("utf-8"),
                    user['RoleId'],
                    user['SucursalId']
                ))
                conn.commit()
                cur.close()
                db_pool.putconn(conn)
        return True


    def get_user_list(self, num_offset, sucursal_id):
        with db_pool.getconn() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                           select tu.nombre , tu.apellido , tu.correo , tu.cedula from tb_user tu 
                            where tu.sucursalid = %s
                            order by tu.id 
                            limit 10 offset %s;
                            """,(
                                sucursal_id,
                                num_offset,
                                ))
                users= cur.fetchall()
        return users
    
    
    def get_user_list_restaurant(self, num_offset, restaurant_id):
                with db_pool.getconn() as conn:
                    with conn.cursor(cursor_factory=RealDictCursor) as cur:
                        cur.execute("""
                                select tu.nombre , tu.apellido , tu.correo ,tu.activo, tu.cedula from tb_user tu 
                                    where tu.restauranid = %s
                                    order by tu.id 
                                    limit 10 offset %s;
                                    """,(
                                        restaurant_id,
                                        num_offset,
                                        ))
                        users= cur.fetchall()
                return users
    
    

