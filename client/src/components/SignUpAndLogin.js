// SignUpAndLogin.js
import React from 'react';
import SignUp from './SignUp';
import Login from './Login';
import Header from "./Header"

function SignUpAndLogin() {
  return (
    <div style={{ 
      display: 'flex', 
      flexDirection: 'column', 
      alignItems: 'center', 
      justifyContent: 'center', 
      height: '100vh',
      background: 'linear-gradient(to bottom, lightpink, white)'  
    }}>
      <Header/>
      <SignUp />
      <Login />
    </div>
  );
}

export default SignUpAndLogin;

