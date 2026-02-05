import { BASE_URL } from "@/app/services/auth.service";
import axios from "axios";
import { useEffect, useState } from "react";

type ModalProps = {
    showModal: boolean;
    onClose: () => void;

};

interface Rol {
    id: number
    nombre: string
};

interface Branch {
    id: number
    address: string
};

function NewUserModal(ModalProps: ModalProps) {
    const [rolList, setRolList] = useState<Rol[]>([])
    const [branchList, setBranchList] = useState<Branch[]>([])
    const [cedula, setCedula] = useState("")
    const [nombre, setNombre] = useState("")
    const [apellido, setApellido] = useState("")
    const [correo, setCorreo] = useState("")
    const [cargo, setCargo] = useState(0)
    const [sucursal, setSucursal] = useState<number | null>(null)
    const [errorMessage, setErrorMessage] = useState("")


    async function getRolesAndBranches() {
        try {
            const res = await axios.get(`${BASE_URL}/user/roles-and-branches`,
                {
                    withCredentials: true
                }
            )
            setRolList(res.data.roles)
            setBranchList(res.data.branches)
        }
        catch (err) {
            setErrorMessage("No se logro cargar los datos ")
        }

    }

    useEffect(() => {
        getRolesAndBranches()

        return () => {
            setRolList([])
            setBranchList([])
        }
    }, []);

    async function fetchNewUser() {
        try{const res = await axios.post(`${BASE_URL}/user/new`,
            {
                cedula,
                nombre,
                apellido,
                correo,
                role_id: cargo,
                sucursal_id: sucursal
            },
            {
                withCredentials: true
            }
        )
        ModalProps.onClose()}
        catch(e){
            setErrorMessage("Datos erroneos o ya usados por otro usuario")
        }
    }


    return (
        <dialog id="my_modal_1" className="modal" open={ModalProps.showModal}>
            <form onSubmit={(e) => { e.preventDefault(); fetchNewUser() }}>

                <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
                    <p>{errorMessage}</p>
                    <legend className="fieldset-legend">Registro de Usuario</legend>

                    <label className="label">Cédula</label>
                    <input
                        onChange={(e) => setCedula(e.target.value)}
                        type="text" className="input" placeholder="Cédula" name="cedula" />

                    <label className="label">Nombre</label>
                    <input
                        onChange={(e) => setNombre(e.target.value)}
                        type="text" className="input" placeholder="Nombre" name="nombre" />

                    <label className="label">Apellido</label>
                    <input
                        onChange={(e) => setApellido(e.target.value)}
                        type="text" className="input" placeholder="Apellido" name="apellido" />

                    <label className="label">Correo</label>
                    <input
                        onChange={(e) => setCorreo(e.target.value)}
                        type="email" className="input" placeholder="Correo" name="correo" />

                    <label className="label">Cargo</label>
                    <select
                        onChange={(e) => { setCargo(Number(e.target.value)); if (Number(e.target.value) === 1) { setSucursal(null) } }}
                        defaultValue="Seleccionar Cargo" className="select">
                        <option disabled={true}>Seleccionar Cargo</option>
                        {rolList.map((rol) => (
                            <option key={rol.id} value={rol.id}>{rol.nombre}</option>
                        ))}
                    </select>
                    <label className="label">Sucursal </label>
                    <select value={sucursal ?? ""} disabled={cargo === 1} onChange={(e) => setSucursal(Number(e.target.value))} className="select">
                        <option value="" disabled={true}>Seleccionar Sucursal</option>
                        {branchList.map((sucursal) => (
                            <option key={sucursal.id} value={sucursal.id}>{sucursal.address}</option>
                        ))}
                    </select>
                </fieldset>

                <button className="btn">Agregar</button>
                <button onClick={ModalProps.onClose} className="btn">Cancelar</button>
            </form>

        </dialog>
    )
}

export default NewUserModal