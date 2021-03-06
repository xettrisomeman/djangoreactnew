import React, {useState} from 'react'
import { Layout, Menu, Icon } from 'antd';
import {Link} from 'react-router-dom';

const { Header, Sider, Content } = Layout;

const CustomLayout = props =>{

    const [collapse , setCollapse] = useState(false);

    const toggle = () => {
    setCollapse(!collapse)
    };

    return (
      <Layout>
        <Sider trigger={null} collapsible collapsed={collapse}>
          <div className="logo" />
          <Menu theme="dark" mode="inline" defaultSelectedKeys={['1']}>
            <Menu.Item key="1">
              <span><Link to='/'>Nav 1</Link></span>
            </Menu.Item>
          </Menu>
        </Sider>
        <Layout>
          <Header style={{ background: '#fff', padding: 0 }}>
            <Icon
              className="trigger"
              type={collapse ? 'menu-unfold' : 'menu-fold'}
              onClick={toggle}
            />
          </Header>
          <Content
            style={{
              margin: '24px 16px',
              padding: 24,
              background: '#fff',
              minHeight: 280,
            }}
          >
            {props.children}
          </Content>
        </Layout>
      </Layout>
    );
}


export default CustomLayout;
