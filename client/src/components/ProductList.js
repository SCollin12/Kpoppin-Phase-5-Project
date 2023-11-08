import React, { useEffect, useState } from 'react';
import { Card, Button, Row, Col, Modal } from 'antd';
import './ProductList.css';
import Cart from './Cart'; // Import the Cart component
import ProductForm from './ProductForm'; // Import the ProductForm component

const ProductList = () => {
  const [products, setProducts] = useState([]);
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [hoveredProduct, setHoveredProduct] = useState(null);
  const [showKpop, setShowKpop] = useState(true);
  const [cart, setCart] = useState([]); // State to manage the cart
  const [productReviews, setProductReviews] = useState([]);
  const [modalVisible, setModalVisible] = useState(false);
  const [cartVisible, setCartVisible] = useState(false); // State to manage the cart visibility

  // Use an object to track the "Added" state for each product
  const [addedToCartMap, setAddedToCartMap] = useState({});

  const handleProductAdded = (newProduct) => {
    setProducts([...products, newProduct]);
  };

  useEffect(() => {
    fetch('/products')
      .then((response) => response.json())
      .then((data) => {
        setProducts(data);
      });
  }, []);

  const handleProductSelect = (product) => {
    setSelectedProduct(product);
    setModalVisible(true);

    // Fetch reviews associated with the selected product
    fetch(`/reviews/product/${product.id}`)
      .then((response) => response.json())
      .then((data) => {
        setProductReviews(data);
      });
  };

  const toggleProducts = () => {
    setShowKpop(!showKpop);
  };

  const handleAddToCart = (product) => {
    // Add the selected product to the cart
    setCart([...cart, product]);

    // Set the "Added" state to true for this product
    setAddedToCartMap({
      ...addedToCartMap,
      [product.id]: true,
    });
  };

  const handleRemoveFromCart = (productId) => {
    // Remove the selected product from the cart
    setCart(cart.filter((item) => item.id !== productId));

    // Reset the "Added" state for this product
    setAddedToCartMap({
      ...addedToCartMap,
      [productId]: false,
    });
  };

  const handleClearCart = () => {
    setCart([]);
    setAddedToCartMap({});
   };

  const filteredProducts = showKpop
    ? products.filter((product) => product.type === 'kpop')
    : products.filter((product) => product.type === 'anime');

    return (
      <div style={showKpop ? { background: 'linear-gradient(to right, #006400, #90EE90)' } : { background: 'linear-gradient(to right, darkred, black)' }}>
        <div style={{ position: 'relative', textAlign: 'center' }}>
          <Button onClick={() => setCartVisible(true)} style={{ position: 'absolute', top: '10px', right: '10px' }}>View Cart</Button>
        </div>
        <h2 style={{ textAlign: 'center', fontSize: '36px' }}>November's Inventory </h2>
        <Button onClick={toggleProducts} style={{ fontSize: '18px' }}>
          {showKpop ? 'Show Anime Products' : 'Show K-pop Products'}
        </Button>

      <Row gutter={16}>
        {filteredProducts.map((product) => (
          <Col key={product.id} span={6}>
            <div
              className="product-card"
              onMouseEnter={() => setHoveredProduct(product)}
              onMouseLeave={() => setHoveredProduct(null)}
            >
              <div className="card-image" onClick={() => handleProductSelect(product)}>
                <img alt={product.name} src={product.image_url} />
              </div>
              <div className="card-details">
                {hoveredProduct === product && (
                  <div className="product-tooltip">
                    <p>Price: {product.price}</p>
                    <p>Release Date: {product.release_date}</p>
                    <p>Description: {product.description}</p>
                  </div>
                )}
              </div>
              <Button
                onClick={() => handleAddToCart(product)}
                disabled={addedToCartMap[product.id]} // Disable the button if the product is added
              >
                {addedToCartMap[product.id] ? 'Added' : 'Add to Cart'}
              </Button>
            </div>
          </Col>
        ))}
      </Row>

      {/* Add new product form */}
      <ProductForm onProductAdded={handleProductAdded} />

      {/* Modal for displaying additional product information */}
      <Modal
        title={selectedProduct ? selectedProduct.name : ''}
        visible={modalVisible}
        onCancel={() => setModalVisible(false)}
        footer={null}
      >
        {selectedProduct && (
          <div>
            <p>Price: {selectedProduct.price}</p>
            <p>Release Date: {selectedProduct.release_date}</p>
            <p>Description: {selectedProduct.description}</p>
            <Button
              onClick={() => handleAddToCart(selectedProduct)}
              disabled={addedToCartMap[selectedProduct.id]}
            >
              {addedToCartMap[selectedProduct.id] ? 'Added' : 'Add to Cart'}
            </Button>
            <h3>Product Reviews</h3>
            <ul>
              {productReviews.map((review) => (
                <li key={review.id}>{review.comments}</li>
              ))}
            </ul>
          </div>
        )}
      </Modal>

      {/* Cart component */}
      <Cart visible={cartVisible} onClose={() => setCartVisible(false)} cartItems={cart} removeFromCart={handleRemoveFromCart} clearCart={handleClearCart} />
    </div>
  );
};

export default ProductList;