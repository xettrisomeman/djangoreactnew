import React from 'react';
import 'antd/dist/antd.css';
import {BrowserRouter} from 'react-router-dom';


import CustomLayout from './containers/Layout';
import CustomRoute from './router';

function App(){

  return (
    <BrowserRouter>
     <CustomLayout>
       <CustomRoute/>
     </CustomLayout>
     </BrowserRouter>
  );
}

export default App;
