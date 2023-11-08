import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from './AuthContext';

function AuthLinks() {
  const { isUserLoggedIn } = useAuth();

  return isUserLoggedIn ? (
    <li>
      <Link to="/my-account">My Account</Link>
    </li>
  ) : null;
}

export default AuthLinks;


