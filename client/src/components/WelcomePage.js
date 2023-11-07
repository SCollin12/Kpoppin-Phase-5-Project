import React from 'react';
import { Link } from 'react-router-dom';
import { Card } from 'antd'; // Import Card from antd
import './WelcomePage.css'; // Import CSS file for styling

function WelcomePage() {
  const welcomeImageUrl = "https://image.spreadshirtmedia.com/image-server/v1/products/T1459A839PA3861PT28D1035917970W10000H9000/views/1,width=378,height=378,appearanceId=839,backgroundColor=F2F2F2/finger-heart-i-love-you-hand-sign-gesture.jpg";

  return (
    <div className="welcome-container">
      <h1>Welcome to Your Website</h1>
      <p>Discover amazing products and more!</p>
      <Link to="/signup-login">
        <img
          src={welcomeImageUrl}
          alt="Get Started"
          className="welcome-image"
        />
      </Link>
    </div>
  );
}

export default WelcomePage;




