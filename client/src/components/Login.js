import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Form, Input, Button } from 'antd';
import { useAuth } from './AuthContext';  // Import the useAuth hook

const Login = () => {
  const [form] = Form.useForm();
  const [loginError, setLoginError] = useState('');
  const { setIsUserLoggedIn } = useAuth();  // Get the setIsUserLoggedIn function

  const history = useHistory();

  const handleLoginSubmit = async (values) => {
    fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then((res) => {
        if (res.status === 201) {
          return res.json().then((data) => {
            setIsUserLoggedIn(true);  // Set isUserLoggedIn to true
            history.push('/products');
          });
        } else if (res.status === 400) {
          setLoginError('Username or password is incorrect');
          return Promise.reject('Authentication failed');
        }
      })
      .catch((error) => {
        console.error('Authentication failed', error);
      });
  };

  return (
    <div style={{ 
      background: 'linear-gradient(to bottom, #0072ff, lightpink)', 
      padding: '40px', 
      borderRadius: '10px',
      width: '100%',
      maxWidth: '500px'  // Limit the width of the form
    }}>
      <h2>Login</h2>
      <Form form={form} onFinish={handleLoginSubmit} style={{ width: '100%' }}>
        <Form.Item label="Username" name="username" rules={[{ required: true, message: 'Please input your username!' }]}>
          <Input placeholder="Username" />
        </Form.Item>
        <Form.Item label="Password" name="password" rules={[{ required: true, message: 'Please input your password!' }]}>
          <Input.Password placeholder="Password" />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">Login</Button>
        </Form.Item>
      </Form>
      {loginError && <p style={{ color: 'red' }}>{loginError}</p>}
    </div>
  );
};

export default Login;
