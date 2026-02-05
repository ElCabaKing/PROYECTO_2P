import { useState } from "react"
import axios from "axios"
export default function useRecovery(){
    const [correo, setCorreo] = useState("")
    const [errorMessage, setErrorMessage] = useState("")
    const [alert, setAlert] = useState("");
    const [showAlert, setShowAlert] = useState(false)

    async function recovery(){
        try{
            const res = await axios.post("http://localhost:5003/auth/recovery_request",
            {
                correo
            })
            console.log(res.data)
            setAlert(res.data.reponse)
            setShowAlert(true)
            setTimeout(() => {
                setShowAlert(false);
                setAlert("");
            }, 3000);
            
        }
        catch(e){
            console.log(e)
        }
    }
    return{
        correo,
        setCorreo,
        errorMessage,
        recovery,
        alert,
        showAlert
    
    }
}