import React from 'react';
import 'antd/dist/antd.css';

import CustomLayout from './containers/Layout';
import PostList from './containers/PostList';


function App(){

  return (
     <CustomLayout>
       <PostList/>
     </CustomLayout>
  );
}

export default App;
