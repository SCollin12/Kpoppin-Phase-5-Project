import React, { useState } from 'react';
import { useHistory } from 'react-router-dom';

const Login = () => {
  const [loginForm, setLoginForm] = useState({
    username: '',
    password: '',
  });

  const [loginError, setLoginError] = useState('');

  const history = useHistory();

  const handleLoginChange = (e) => {
    const name = e.target.name;
    const value = e.target.value;
    setLoginForm({
      ...loginForm,
      [name]: value,
    });
  };

  const handleLoginSubmit = (event) => {
    event.preventDefault(); // Prevent the default form submission

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
        // Check if the response data contains the user data
        if (data.id) {
          // Redirect to the desired page upon successful login
          history.push('/products'); // Replace 'desired-page' with your target route
        }
      })
      .catch((error) => {
        console.error('Authentication failed', error);
      });
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLoginSubmit}>
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            name="username"
            value={loginForm.username}
            onChange={handleLoginChange}
          />
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            name="password"
            value={loginForm.password}
            onChange={handleLoginChange}
          />
        </div>
        <div>
          <button type="submit">Login</button>
        </div>
      </form>
      {loginError && <p style={{ color: 'red' }}>{loginError}</p>}
    </div>
  );
};

export default Login;

