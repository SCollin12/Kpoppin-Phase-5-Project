import React from 'react';
import { Card, Button } from 'antd';


const ProductList = ({ products, onProductSelect }) => {
  return (
    <div>
      {products.map((product) => (
        <Card
          key={product.id}
          title={product.name}
          extra={<Button onClick={() => onProductSelect(product)}>View Details</Button>}
        >
          <p>Description: {product.description}</p>
          <p>Price: ${product.price}</p>
        </Card>
      ))}
    </div>
  );
};

export default ProductList;
