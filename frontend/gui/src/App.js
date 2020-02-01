import React , {useEffect} from 'react';
import 'antd/dist/antd.css';
import axios from 'axios';

import CustomLayout from './containers/Layout';


function App() {

  useEffect(()=>{
    axios.get('http://localhost:8000/api/')
    .then((res=>{
      console.log(res.data)
    }))
    .catch(error=>console.log(error));
  },[])
  return (
     <CustomLayout>

     </CustomLayout>
  );
}

export default App;
