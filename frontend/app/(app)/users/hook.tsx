'use client'
import { useState } from "react"
import axios from "axios";
import {User} from "../../types/types";

export default function useUsers() {
    const [userList, setUserList] = useState<User[]>([]);
    const [numIndex, setnumIndex] = useState(1);
    const [showModal, setShowModal] = useState(false);
    const [maxIndex, setmaxIndex] = useState(1)
    
    async function fetchUsers() {
        const res = await axios.get("/api/security/user/list",
            {
                params :{
                    index_num: numIndex
                },
                withCredentials: true
            }
        )
        setUserList(res.data.users);
        setmaxIndex(res.data.max_index)
        
    }
    return {
        userList,
        fetchUsers,
        showModal,
        setShowModal,
        numIndex,
        setnumIndex,
        maxIndex
    }
}

