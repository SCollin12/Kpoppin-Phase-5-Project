import React, { useState, useEffect } from 'react';

const OrderList = () => {
  const [orders, setOrders] = useState([]);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Fetch a list of orders from your Flask API
    fetch('/orders')
      .then((response) => response.json())
      .then((data) => {
        setOrders(data);
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  return (
    <div>
      <h2>Order List</h2>
      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>User ID</th>
            <th>Status</th>
            <th>Products</th>
          </tr>
        </thead>
        <tbody>
          {orders.map((order) => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.user_id}</td>
              <td>{order.status}</td>
              <td>
                <ul>
                  {order.order_products.map((orderProduct) => (
                    <li key={orderProduct.id}>
                      Product ID: {orderProduct.product_id}
                      {/* You can fetch and display more product information here */}
                    </li>
                  ))}
                </ul>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default OrderList;
