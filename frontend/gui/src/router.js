import React from 'react';
import {Route} from 'react-router-dom';

import PostList from './containers/PostList';
import PostDetail from './containers/PostDetail';


const CustomRoute = ()=>{

    return(
        <div>
            <Route exact path='/' component={PostList}/>
            <Route exact path='/:postID' component={PostDetail}/>
        </div>
    )
}

export default CustomRoute;