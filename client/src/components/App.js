import React from 'react';
import { BrowserRouter, Route, Link } from 'react-router-dom';
import NavigationBar from './NavigationBar'; // Import the NavigationBar component
import Homepage from './Homepage';
import ReviewForm from './ReviewForm';
import ProductList from './ProductList';
import OrderList from './OrderList';
import SignUpAndLogin from './SignUpAndLogin';
import WelcomePage from './WelcomePage';

function App() {
  return (
    <BrowserRouter>
      <NavigationBar /> {/* Include the NavigationBar outside of the Route component */}
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/reviews">Reviews</Link>
            </li>
            <li>
              <Link to="/products">Products</Link>
            </li>
            <li>
              <Link to="/orders">Orders</Link>
            </li>
            <li>
              <Link to="/signup-login">Sign Up / Login</Link>
            </li>
          </ul>
        </nav>

        <Route path="/" exact component={WelcomePage} />
        <Route path="/reviews" component={ReviewForm} />
        <Route path="/products" component={ProductList} />
        <Route path="/orders" component={OrderList} />
        <Route path="/signup-login" component={SignUpAndLogin} />
        <Route path="/home" component={Homepage} />
      </div>
    </BrowserRouter>
  );
}

export default App;









































// // App.js
// import React, { useState, useEffect } from 'react';
// import Main from './components/Main';
// import Login from './components/Login';
// import Signup from './components/Signup';
// import ProductDetails from './components/ProductDetails';
// import Cart from './components/Cart';
// import Homepage from './components/Homepage';
// import { Switch, Route, Routes } from 'react-router-dom';

// function App() {
//   const [user, setUser] = useState('');

//   useEffect(() => {
//     // Fetch user data or check if the user is authenticated
//     // Set the user state accordingly
//   }, []);

//   return (
//     <div className='App'>
//       <h1>Project Client</h1>
//       <Routes>
//         <Route path='/' element={<Login userToDisplay={setUser} />} />
//         <Route path='/signup' element={<Signup userToDisplay={setUser} />} />
//         <Route path='/home' element={<Homepage />} />
//         <Route path='/product/:id' element={<ProductDetails />} />
//         <Route path='/cart' element={<Cart />} />
//       </Routes>
//     </div>
//   );
// }

// export default App;

