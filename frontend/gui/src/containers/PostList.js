import React , {useState , useEffect} from 'react'
import axios from 'axios';

import Posts from '../components/Posts';

const PostList = ()=>{
    const [data, setData] = useState([]);

    useEffect(()=>{
        axios.get('http://localhost:8000/api/')
        .then((res)=>{
            setData(res.data)
        })
        .catch(err=>console.log(err))
    },[])

    return(
        <Posts data={data}/>
    )
}

export default PostList;