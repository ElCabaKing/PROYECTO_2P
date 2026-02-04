"use client"
import useApp from "./hook"

export default function LogIn() {
    const { setCedula, cedula, password, setPassword, logIn, errorMessage, showError } = useApp()
    return (
        <div className="flex min-h-screen items-center justify-center">
            <div className="card card-side bg-base-100 shadow-sm">
                <figure className="p-4 bg-amber-50">
                    <img
                        src="https://upload.wikimedia.org/wikipedia/commons/6/6d/LogoUGcolor.png"
                        alt="Ug"
                        className="w-24 h-auto object-contain" />


                </figure>
                <div className="card-body bg-amber-50 rounded-r-lg">
                    <form onSubmit={(e) => { e.preventDefault(); logIn() }}>
                        <fieldset className="fieldset bg-base-200 border-base-300 rounded-box w-xs border p-4">
                            <p className="text-red-500 text-sm min-h-5">
                                {errorMessage}
                            </p>

                            <label className="label">Cedula</label>
                            <input type="text" className="input"
                                placeholder="Cedula"
                                onChange={(e) => setCedula(e.target.value)}
                                value={cedula}
                                required />

                            <label className="label">Contrasena</label>
                            <input type="password"
                                className="input"
                                placeholder="Contrasena"
                                onChange={(e) => setPassword(e.target.value)}
                                value={password}
                                required />


                            <a href="http://localhost:3000/recovery-page" className="link">Olvidaste la contraseña?</a>

                            <button className="btn w-64 rounded-full">Button</button>
                        </fieldset>
                    </form>
                </div>
            </div>
        </div >
    )
}