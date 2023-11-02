
import React, { useState, useEffect } from 'react';
import Main from './components/Main';
import Login from './components/Login';
import Signup from './components/Signup';
import ProductDetails from './components/ProductDetails'; // New component for product details
import Cart from './components/Cart'; // New component for cart
import { Switch ,Route, Routes } from 'react-router-dom';

function App() {
  const [user, setUser] = useState('');
  
  useEffect(() => {
    fetch('/auto_login')
    .then((res) => res.json())
    .then((data) => setUser(data))
    .catch((error) => console.error('Error fetching user data:', error));
  }, []);
  
  return (
    <div className='App'>
      <h1>Project Client</h1>;
      <Routes>
        <Route path='/' element={<Login userToDisplay={setUser} />} />
        <Route path='/signup' element={<Signup userToDisplay={setUser} />} />
        <Route path='/home' element={<Main user={user} setUser={setUser} />} />
        <Route path='/product/:id' element={<ProductDetails />} />
        <Route path='/cart' element={<Cart />} />
      </Routes>
    </div>
  );
}

export default App;
