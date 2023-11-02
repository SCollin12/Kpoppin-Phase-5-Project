import React from 'react';
import { Form, Input, Button } from 'antd';

const Login = () => {
  // Implement login logic here
  return (
    <div>
      <h2>Login</h2>
      <Form
        name="login"
        onFinish={(values) => {
          // Handle login form submission
          console.log('Received values:', values);
        }}
      >
        <Form.Item name="email" label="Email">
          <Input />
        </Form.Item>
        <Form.Item name="password" label="Password">
          <Input.Password />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">
            Login
          </Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default Login;
