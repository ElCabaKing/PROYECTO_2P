"use client"
import { useState } from "react"
import axios from "axios"
import { useRouter } from "next/navigation"


export default function useApp() {
    const [cedula, setCedula] = useState("")
    const [password, setPassword] = useState("")
    const [showError, setShowError] = useState(false)
    const [errorMessage, setErrorMessage] = useState(" ")
    const router = useRouter()


    async function logIn() {
        try {
            const log = await axios.post("http://localhost:5003/auth/logIn",
                {
                    cedula,
                    contrasena: password
                }
            )
            if(log.data.logIn){
                router.push("/home")
            }
        }
        catch (e: unknown) {
            if (axios.isAxiosError(e)) {
                setErrorMessage(e.response?.data.details)
                console.log(e.response?.data)
                setShowError(true)
            } else {
                console.log("ERROR DESCONOCIDO:", e)
            }
        }


    }

    return {
        setCedula,
        cedula,
        password,
        setPassword,
        logIn,
        errorMessage,
        showError
    }
}