import React ,{useState , useEffect} from 'react';
import axios from 'axios';



const PostDetail = props=>{
    const [post , setPost] = useState({})

    useEffect(()=>{
        const id = props.match.params.postID
        axios.get(`http://localhost:8000/api/${id}/`)
        .then((res)=>{
            console.log(res.data)
            setPost(res.data)
        })
        .catch(err=>console.log(err))
    },[])
    return(
        <div>
        <p>{post.title}</p>
        <p>{post.content}</p>
        </div>
    )
}

export default PostDetail;