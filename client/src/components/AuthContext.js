import React, { createContext, useContext, useState } from 'react';

const AuthContext = createContext();

export function useAuth() {
  return useContext(AuthContext);
}

export function AuthProvider({ children }) {
  const [isUserLoggedIn, setIsUserLoggedIn] = useState(false);

  // Your authentication logic and state management here

  const value = {
    isUserLoggedIn,
    setIsUserLoggedIn, // Include the function to set authentication status
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}
