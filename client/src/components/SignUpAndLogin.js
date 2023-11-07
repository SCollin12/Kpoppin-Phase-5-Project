import React from 'react';
import SignUp from './SignUp';
import Login from './Login';

function SignUpAndLogin() {
  return (
    <div>
      <div className="signup-and-login-container">
        <div className="signup-section">
          <SignUp />
        </div>
        <div className="login-section">
          <Login />
        </div>
      </div>
    </div>
  );
}

export default SignUpAndLogin;
