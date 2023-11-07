import React from 'react';
import { Link } from 'react-router-dom';

const NavigationBar = () => {
  return (
    <nav>
      <ul>
        {/* <li>
          <Link to="/products">Products</Link>
        </li>
        <li>
          <Link to="/reviews">Reviews</Link>
        </li> */}
        <li>
          <Link to="/my-account">My Account</Link> {/* Create a new component for user account settings */}
        </li>
        {/* Add a "Logout" button here */}
      </ul>
    </nav>
  );
};

export default NavigationBar;
