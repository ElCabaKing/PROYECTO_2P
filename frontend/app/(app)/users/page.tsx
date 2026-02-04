'use client'
import useUsers from "./hook"
import { useEffect } from "react"
import NewUserModal from "./NewUserModal"

function page() {
  const { userList, fetchUsers, showModal, setShowModal, numIndex, setnumIndex, maxIndex} = useUsers()


  useEffect(() => {
    fetchUsers()
  }, [numIndex])

  return (
    <div>
      <div className="overflow-x-auto">
        <table className="table">
          <thead>
            <tr>
              <th>Usuario</th>
              <th>Rold</th>
              <th>Sucursal</th>
              <th><button className="btn" onClick={() => setShowModal(true)}>+</button></th>
            </tr>
          </thead>
          <tbody>
            {userList.map((user) => (
              <tr key={user.cedula}>
                <td>
                  <div className="flex items-center gap-3">
                    <div>
                      <div className="font-bold">{user.nombre} {user.apellido}</div>
                      <div className="text-sm opacity-50">{user.cedula}</div>
                    </div>
                  </div>
                </td>
                <td>
                  <span className="badge badge-ghost badge-sm">{user.rol_nombre}</span>
                </td>
                <td>{user.direccion}</td>
                <th>
                  <button className="btn btn-ghost btn-xs">detalles</button>
                </th>
              </tr>))}
          </tbody>
        </table>
      </div>
      <div className="join">
        <button disabled={numIndex === 1} onClick={() => {numIndex===1? '': setnumIndex(numIndex - 1) }} className="join-item btn">«</button>
        <button className="join-item btn">Page {numIndex}</button>
        <button disabled={numIndex === maxIndex} onClick={() => {numIndex===maxIndex? '': setnumIndex(numIndex + 1) }} className="join-item btn">»</button>
      </div>
      {showModal && <NewUserModal showModal={showModal} onClose={() => { fetchUsers(); setShowModal(false) }} />}
    </div>
  )
}

export default page