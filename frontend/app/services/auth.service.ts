import axios from "axios"

const BASE_URL = 'http://localhost/api/security'
export const authService = {

    ServicelogIn: async (cedula: string, password: string) => {

        const log = await axios.post(`${BASE_URL}/auth/logIn`,
            {
                cedula,
                contrasena: password
            },
            {
                withCredentials: true
            })
        return log.data
    }
}