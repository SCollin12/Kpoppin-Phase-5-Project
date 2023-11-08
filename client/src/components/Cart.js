import React, { useState } from 'react';
import { Drawer, List, Button, Modal } from 'antd';

const Cart = ({ visible, onClose, cartItems, removeFromCart, clearCart }) => {
  const [checkoutSuccess, setCheckoutSuccess] = useState(false);
  const totalItems = cartItems.length;
  const totalPrice = cartItems.reduce((acc, item) => {
    const itemPrice = parseFloat(item.price);
    return isNaN(itemPrice) ? acc : acc + itemPrice;
  }, 0);

 const handleCheckout = () => {
  // Perform the checkout logic here (e.g., making an API request)

  // Create an array of product IDs from cartItems
  const productIds = cartItems.map((item) => item.id);

  // Send a POST request to create a new order
  fetch('/orders', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      user_id: 1, // Replace with the actual user ID
      product_ids: productIds, // Send the product IDs in an array
    }),
  })
    .then((response) => {
      if (response.status === 201) {
        // Order created successfully, you can add additional logic here
        console.log('Order created successfully.');

        // Assuming the checkout is successful, set checkoutSuccess to true
        setCheckoutSuccess(true);
        clearCart();
 
      } else {
        // Handle errors or display appropriate messages
        console.error('Failed to create an order.');
      }
    })
    .catch((error) => {
      console.error('API request error:', error);
    });
};


  const closeCheckoutModal = () => {
    setCheckoutSuccess(false);
    // You can also perform any additional actions here if needed
  };

  return (
    <Drawer
      title="Shopping Cart"
      placement="right"
      closable={true}
      onClose={onClose}
      visible={visible}
      width={300}
    >
      <List
        dataSource={cartItems}
        renderItem={(item) => (
          <List.Item key={item.id}>
            <span>{item.name}</span>
            <Button onClick={() => removeFromCart(item.id)} type="danger">
              Remove
            </Button>
          </List.Item>
        )}
      />
      {totalItems > 0 && 
        <div>
          <p>
            Total Items: {totalItems}
            <br />
            Total Price: $ {totalPrice.toFixed(2)}
          </p>
          <Button onClick={handleCheckout} type="primary">
            Checkout
          </Button>
        </div>
      }

      <Modal
        title="Checkout Successful"
        visible={checkoutSuccess}
        onOk={closeCheckoutModal}
        onCancel={closeCheckoutModal}
      >
        <p>Your order has been successfully placed.</p>
      </Modal>
    </Drawer>
  );
};

export default Cart;
