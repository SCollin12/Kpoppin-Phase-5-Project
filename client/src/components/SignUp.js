import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';
import { Form, Input, Button } from 'antd';

const SignUp = () => {
  const [form] = Form.useForm();
  const [signupSuccess, setSignupSuccess] = useState(null);
  const [signupError, setSignupError] = useState(null);

  const history = useHistory();

  const handleSubmit = async (values) => {
    fetch('/signup', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(values),
    })
      .then((res) => {
        if (res.status === 201) {
          setSignupSuccess('Signup successful. You can now log in.');
          setSignupError(null);
          // Clear the form
          form.resetFields();
        } else {
          return res.json().then((data) => {
            setSignupError(data.error);
            setSignupSuccess(null);
          });
        }
      })
      .catch((error) => {
        console.error('Error:', error);
        setSignupError('An error occurred during signup.');
        setSignupSuccess(null);
      });
  };

  return (
    <div style={{ 
      background: 'linear-gradient(to bottom, lightpink, #00c6ff)', 
      padding: '40px', 
      borderRadius: '10px',
      width: '100%',
      maxWidth: '500px'  // Limit the width of the form
    }}>
      <h2>Sign Up</h2>
      <Form form={form} onFinish={handleSubmit} style={{ width: '100%' }}>
        <Form.Item label="Username" name="username" rules={[{ required: true, message: 'Please input your username!' }]}>
          <Input placeholder="Username" />
        </Form.Item>
        <Form.Item label="Email" name="email" rules={[{ required: true, message: 'Please input your email!' }]}>
          <Input placeholder="Email" />
        </Form.Item>
        <Form.Item label="Password" name="password" rules={[{ required: true, message: 'Please input your password!' }]}>
          <Input.Password placeholder="Password" />
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">Sign Up</Button>
        </Form.Item>
      </Form>
      {signupSuccess && <p style={{ color: 'green' }}>{signupSuccess}</p>}
      {signupError && <p style={{ color: 'red' }}>{signupError}</p>}
    </div>
  );
};

export default SignUp;






