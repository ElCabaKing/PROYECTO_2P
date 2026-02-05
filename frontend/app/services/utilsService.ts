
import { LayoutData } from "@/app/types/types"
import axios from "axios"

export async function getLayoutData(): Promise<LayoutData> {
  try{const res = await axios.get('/api/security/user/profile',
    {
        withCredentials: true,
    }
  )
    console.log(res.data)
    return res.data}
    catch(e){
        console.log(e)
        return {
            user: null
        }   
    }
}
