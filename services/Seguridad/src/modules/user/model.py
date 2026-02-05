from src.config.db import db_pool
from psycopg2.extras import RealDictCursor

class UserModel():

    def insert_new_user(self, user, restaurant_id):
        print(user)
        conn = db_pool.getconn()
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO usuarios
                    (cedula, nombre, apellido, correo, contrasena_hash, role_id, sucursal_id, restaurante_id)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                """, (
                    user['cedula'],
                    user['nombre'],
                    user['apellido'],
                    user['correo'],
                    user['contrasena'].decode("utf-8"),
                    user['role_id'],
                    user['sucursal_id'],
                    restaurant_id,
                ))
                conn.commit()
            return True
        finally:
            cur.close()
            db_pool.putconn(conn)


    def get_user_list(self, num_offset, sucursal_id):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                           select ts.address, tu.nombre , tu.apellido , tu.correo ,tu.is_active, tu.cedula, tu.role_id, tr.nombre as rol_nombre from usuarios tu 
                            JOIN roles tr ON tu.role_id = tr.id
                            JOIN sucursales ts ON tu.sucursal_id = ts.id
                            where tu.sucursal_id = %s
                            order by tu.id 
                            limit 6 offset %s;
                            """,(
                                sucursal_id,
                                num_offset,
                                ))
                users= cur.fetchall()
                print(users)
            return users
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_user_count(self, sucursal_id):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT COUNT(*) as total FROM usuarios
                    WHERE sucursal_id = %s;
                """, (sucursal_id,))
                result = cur.fetchone()
            return result['total'] if result else 0
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    
    def get_user_list_restaurant(self, num_offset, restauran_id):
  
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                        select ts.address, tu.nombre , tu.apellido , tu.correo ,tu.is_active, tu.cedula, tu.role_id, tr.nombre as rol_nombre from usuarios tu 
                            JOIN roles tr ON tu.role_id = tr.id
                            LEFT JOIN sucursales ts ON tu.sucursal_id = ts.id
                            where tu.restaurante_id = %s
                            order by tu.id 
                            limit 6 offset %s;
                            """,(
                                restauran_id,
                                num_offset,
                                ))
                users= cur.fetchall()
            return users
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_user_count_restaurant(self, restaurant_id):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT COUNT(*) as total FROM usuarios
                    WHERE restaurante_id = %s;
                """, (restaurant_id,))
                result = cur.fetchone()
            return result['total'] if result else 0
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_user_by_id(self, user_id):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, cedula, nombre, apellido, correo, role_id, sucursal_id, restaurante_id, is_active
                    FROM usuarios
                    WHERE id = %s;
                """, (user_id,))
                user = cur.fetchone()
            return user
        finally:
            cur.close()
            db_pool.putconn(conn)

    def update_user(self, user_id, update_data):
        conn = db_pool.getconn()
        try:
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
                    UPDATE usuarios
                    SET {', '.join(set_clause)}
                    WHERE id = %s;
                """
                
                cur.execute(query, tuple(params))
                conn.commit()
            return True
        finally:
            cur.close()
            db_pool.putconn(conn)
    
    def get_all_roles(self):
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, nombre FROM roles
                    ORDER BY id;
                """)
                roles = cur.fetchall()
            return roles
        finally:
            cur.close()
            db_pool.putconn(conn)

    def get_menus_by_role(self, role_id):
        """Obtiene todos los menús disponibles para un rol"""
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT m.id, m.nombre, m.path, m.icono, m.descripcion
                    FROM menus m
                    INNER JOIN rol_menu rm ON m.id = rm.menu_id
                    WHERE rm.role_id = %s AND m.activo = TRUE
                    ORDER BY m.nombre;
                """, (role_id,))
                menus = cur.fetchall()
            return menus
        finally:
            cur.close()
            db_pool.putconn(conn)
    

    def get_branches_by_restaurant(self, restaurant_id):
        """Obtiene todas las sucursales de un restaurante"""
        conn = db_pool.getconn()
        try:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("""
                    SELECT id, address
                    FROM sucursales
                    WHERE restaurante_id = %s
                """, (restaurant_id,))
                branches = cur.fetchall()
            return branches
        finally:
            cur.close()
            db_pool.putconn(conn)