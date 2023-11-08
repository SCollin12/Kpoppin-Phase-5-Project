import React, { useState, useEffect } from 'react';
import { Table } from 'antd';

const OrderList = () => {
 const [orders, setOrders] = useState([]);
 const [isLoading, setIsLoading] = useState(true);
 const [productDetails, setProductDetails] = useState([]);
 const [isProductLoading, setIsProductLoading] = useState(true);

 useEffect(() => {
   fetch('/orders')
     .then((response) => response.json())
     .then((data) => {
       setOrders(data);
       setIsLoading(false);
     });
 }, []);

 useEffect(() => {
   fetch('/products')
     .then((response) => response.json())
     .then((data) => {
       setProductDetails(data);
       setIsProductLoading(false);
     });
 }, []);

 if (isLoading || isProductLoading) {
   return <div>Loading...</div>;
 }

 const columns = [
   {
     title: 'Order ID',
     dataIndex: 'id',
   },
   {
     title: 'User ID',
     dataIndex: 'user_id',
   },
   {
     title: 'Status',
     dataIndex: 'status',
   },
   {
    title: 'Products',
    dataIndex: 'order_products',
    render: (orderProducts) => (
      <ul>
        {orderProducts.map((orderProduct) => {
          const product = productDetails.find(
            (product) => product.id === orderProduct.product_id
          );
          return (
            <li key={orderProduct.id}>
              Product Name: {product ? product.name : 'N/A'}
            </li>
          );
        })}
      </ul>
    ),
  },
];

return (
  <div style={{ background: 'linear-gradient(to right, darkgrey, lightgrey, white)' }}>
    <h2>Customer Orders "From Sept 2023 - Nov -2023 *Admin Use Only*</h2>
    <Table columns={columns} dataSource={orders} />
  </div>
);
};

export default OrderList;