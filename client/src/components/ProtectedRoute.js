import React from 'react';
import { Route, Redirect } from 'react-router-dom';
import { useAuth } from './AuthContext';

function ProtectedRoute({ component: Component, ...rest }) {
  const { isUserLoggedIn } = useAuth();

  return (
    <Route
      {...rest}
      render={props =>
        isUserLoggedIn ? (
          <Component {...props} />
        ) : (
          <Redirect to="/signup-login" />
        )
      }
    />
  );
}

export default ProtectedRoute;
