import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import NavigationBar from './NavigationBar';
import Homepage from './Homepage';
import ReviewForm from './ReviewForm';
import ProductList from './ProductList';
import OrderList from './OrderList';
import SignUpAndLogin from './SignUpAndLogin';
import WelcomePage from './WelcomePage';
import { AuthProvider } from './AuthContext';
import ProtectedRoute from './ProtectedRoute';

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <NavigationBar className="navbar" />

        <Route path="/" exact component={WelcomePage} />
        <ProtectedRoute path="/reviews" component={ReviewForm} />
        <ProtectedRoute path="/products" component={ProductList} />
        <ProtectedRoute path="/orders" component={OrderList} />
        <Route path="/signup-login" component={SignUpAndLogin} />
        <ProtectedRoute path="/home" component={Homepage} />
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
