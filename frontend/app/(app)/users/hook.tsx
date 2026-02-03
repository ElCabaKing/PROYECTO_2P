'use client'
import { useState } from "react"
import axios from "axios";

export default function useUsers() {
    const [userList, setUserList] = useState([]);
    const [numIndex, setnumIndex] = useState(1);
    
    async function fetchUsers() {
        const res = await axios.get("http://localhost:5003/user/list",
            {
                params :{
                    index_num: numIndex
                },
                withCredentials: true
            }
        )
        console.log(res.data.users)
        
    }
    return {
        userList,
        fetchUsers
    }
}

