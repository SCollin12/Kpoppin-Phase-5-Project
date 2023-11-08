import React from 'react';
import { Link } from 'react-router-dom';
import { Typography, Row, Col } from 'antd'; // Import Ant Design components

const { Title, Paragraph, Text } = Typography;

function WelcomePage() {
  const welcomeImageUrl = "https://image.spreadshirtmedia.com/image-server/v1/products/T1459A839PA3861PT28D1035917970W10000H9000/views/1,width=378,height=378,appearanceId=839,backgroundColor=F2F2F2/finger-heart-i-love-you-hand-sign-gesture.jpg";
  const backgroundImageUrl = "https://cdn.openart.ai/stable_diffusion/5ff96d121d1873ed7e01ba63ee091595e4638297_2000x2000.webp";

  return (
    <div className="welcome-container" style={{ 
      backgroundImage: `url(${backgroundImageUrl})`,
      backgroundSize: 'cover',
      backgroundRepeat: 'no-repeat',
      backgroundPosition: 'center',
      height: '110vh'
    }}>
<Row gutter={[16, 16]} style={{ height: '100vh' }}>
 <Col xs={100} sm={100} md={100} style={{ height: '100vh' }}>
   <div style={{ background: 'linear-gradient(to bottom, #FFA500, #FFD700, #FFFF00)', padding: '20px', borderRadius: '10px', height: '100vh' }}>
     <Title style={{ textAlign: 'center', fontFamily: 'Courier New'  }}>Welcome to Kpoppin USA + Anime!!</Title>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px', color: 'red' }}>The #1 Shop for Kpop, Anime & Asian snacks!!</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px', color: 'red'}}>8251 S. John Young Parkway, Orlando, FL 32819 (Sand Lake Shopping Center) Near Walmart, next to Pet Smart</Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px', color: 'red' }}>Phone #: 407-930-3203</Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px', color: 'red' }}>Store hours: (subject to change) Mon-Thurs: 10am-6pm Fri & Sat: 10am-7pm Sun: 10am-6pm</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px', color: 'red'}}>Call us during store hours to reserve an item which can be held for 24 hours.</Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px' }}>For more information visit us on:</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}>Facebook, Instagram, and Twitter:</Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px' }}><Text strong>Facebook:</Text> <a href="www.facebook.com/kpoppinusashop">www.facebook.com/kpoppinusashop</a></Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}><Text strong>Facebook:</Text> <a href="www.facebook.com/kpopconusa">www.facebook.com/kpopconusa</a></Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}><Text strong>Instagram:</Text> kpoppin.usa</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}><Text strong>Twitter:</Text> kpoppinusashop</Paragraph>
            <Paragraph style={{ textAlign: 'center' }}>Also visit our EBAY shop for online purchases!</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}><Text strong>"KPOPPIN USA" shop:</Text> <a href="http://stores.ebay.com/ANIME-BENTO">http://stores.ebay.com/ANIME-BENTO</a></Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px' }}>We have been successfully providing mail orders through EBAY since early 2000's.</Paragraph>
            <Paragraph style={{ textAlign: 'center', fontSize: '20px' }}>We expedite your order same day or next day. Media items are shipped via USPS Ground Advantage (2-5 business days).</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}>Much faster & safer than ordering from overseas.</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}>We are here for YOU! Your local retailer in the USA!</Paragraph>
            <Paragraph style={{ textAlign: 'center' , fontSize: '20px'}}>We need YOUR support to continue providing YOU and the community with the best selection of Korean/KPop/Anime/Japanese Merchandise in the USA!</Paragraph>
          </div>
        </Col>
       <Col xs={100} sm={100} md={100}>
   <Link to="/signup-login">
     <img src={welcomeImageUrl} alt="Get Started" className="welcome-image" />
   </Link>
        </Col>
      </Row>
    </div>
  );
}

export default WelcomePage;






