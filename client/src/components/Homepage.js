import React, { useState } from 'react';
import KpopProducts from './KpopProducts'; // Import K-pop product component
import AnimeProducts from './AnimeProducts'; // Import anime product component

const Homepage = () => {
  const [showKpop, setShowKpop] = useState(true);

  return (
    <div>
      <button onClick={() => setShowKpop(true)}>Show K-pop Products</button>
      <button onClick={() => setShowKpop(false)}>Show Anime Products</button>
      {showKpop ? <KpopProducts /> : <AnimeProducts />}
    </div>
  );
};

export default Homepage;
