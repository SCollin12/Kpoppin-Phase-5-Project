import React, { useState } from 'react';
import { Form, Input, Button } from 'antd';

const Login = () => {
  const [loginForm, setLoginForm] = useState({
    email: '',
    password: '',
  });

  const [loginError, setLoginError] = useState('');

  const handleLoginChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setLoginForm({
      ...loginForm,
      [name]: value,
    });
  };

  const handleLoginSubmit = (e) => {
    e.preventDefault();

    // Send a POST request to your Flask backend for authentication
    fetch('/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(loginForm),
    })
      .then((res) => {
        if (res.status === 201) {
          return res.json();
        } else if (res.status === 400) {
          setLoginError('Username or password is incorrect');
          return Promise.reject('Authentication failed');
        }
      })
      .then((data) => {
        // Redirect to the home page or perform the necessary action upon successful login
        // You can use React Router for navigation
        console.log('Login successful', data);
      })
      .catch((error) => {
        console.error('Authentication failed', error);
      });
  };

  return (
    <div>
      <h2>Login</h2>
      <Form name="login" onFinish={handleLoginSubmit}>
        <Form.Item name="email" label="Email">
          <Input name="email" value={loginForm.email} onChange={handleLoginChange} />
        </Form.Item>
        <Form.Item name="password" label="Password">
          <Input.Password name="password" value={loginForm.password} onChange={handleLoginChange} />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Login
          </Button>
        </Form.Item>
      </Form>
      {loginError && <p style={{ color: 'red' }}>{loginError}</p>}
    </div>
  );
};

export default Login;
