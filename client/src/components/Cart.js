import React from 'react';
import { Drawer, List, Button } from 'antd';

const Cart = ({ visible, onClose, cartItems, removeFromCart }) => {
    const totalItems = cartItems.length;
  
    // Calculate the total price only if cartItems are valid
    const totalPrice = cartItems.reduce((acc, item) => {
      const itemPrice = parseFloat(item.price); // Parse the price to a float
      return isNaN(itemPrice) ? acc : acc + itemPrice;
    }, 0);
  
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
        {totalItems > 0 && (
          <p>
            Total Items: {totalItems}
            <br />
            Total Price: $ {totalPrice.toFixed(2)} {/* Ensure toFixed is called on a number */}
          </p>
        )}
      </Drawer>
    );
  };
  
export default Cart;
