"use client"
import { useState } from "react"
import { useRouter } from "next/navigation"
import {authService} from '../../services/auth.service'


export default function useApp() {
    const [cedula, setCedula] = useState("")
    const [password, setPassword] = useState("")
    const [showError, setShowError] = useState(false)
    const [errorMessage, setErrorMessage] = useState(" ")
    const router = useRouter()


    async function logIn() {
        try {
            const log = await authService.ServicelogIn(cedula, password)
            if(log.logIn){
                router.push("/home")
            }
        }
        catch (e: unknown) {
            console.log(e)
            if (e instanceof Error) {
                setErrorMessage(e.message)
                setShowError(true)
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