// import React, { useState } from 'react';
// import { Card, Button, Form, Input, DatePicker, message } from 'antd';
// import axios from 'axios';

// const ProductDetail = ({ product }) => {
//   const [isEditing, setEditing] = useState(false);
//   const [editedProduct, setEditedProduct] = useState({ ...product });

//   const handleEdit = () => {
//     setEditing(true);
//   };

//   const handleCancel = () => {
//     setEditing(false);
//     setEditedProduct({ ...product });
//   };

//   const handleSave = () => {
//     // Make a PUT request to update the product
//     axios.put(`/products/${product.id}`, editedProduct)
//       .then(response => {
//         setEditing(false);
//         message.success('Product updated successfully');
//       })
//       .catch(error => {
//         message.error('Failed to update product');
//       });
//   };

//   const handleDelete = () => {
//     // Make a DELETE request to delete the product
//     axios.delete(`/products/${product.id}`)
//       .then(response => {
//         message.success('Product deleted successfully');
//         // You can add additional logic to handle UI updates or redirects
//       })
//       .catch(error => {
//         message.error('Failed to delete product');
//       });
//   };

//   return (
//     <div>
//       <Card title={editedProduct.name}>
//         {isEditing ? (
//           <Form>
//             <Form.Item label="Name">
//               <Input
//                 value={editedProduct.name}
//                 onChange={e => setEditedProduct({ ...editedProduct, name: e.target.value })}
//               />
//             </Form.Item>
//             <Form.Item label="Description">
//               <Input.TextArea
//                 value={editedProduct.description}
//                 onChange={e => setEditedProduct({ ...editedProduct, description: e.target.value })}
//               />
//             </Form.Item>
//             <Form.Item label="Price">
//               <Input
//                 value={editedProduct.price}
//                 onChange={e => setEditedProduct({ ...editedProduct, price: e.target.value })}
//               />
//             </Form.Item>
//             <Form.Item label="Release Date">
//               <DatePicker
//                 value={moment(editedProduct.release_date, 'YYYY-MM-DD')}
//                 onChange={date => setEditedProduct({ ...editedProduct, release_date: date.format('YYYY-MM-DD') })}
//               />
//             </Form.Item>
//           </Form>
//         ) : (
//           <div>
//             <p>Description: {editedProduct.description}</p>
//             <p>Price: ${editedProduct.price}</p>
//             <p>Release Date: {editedProduct.release_date}</p>
//           </div>
//         )}
//         <Button type="primary" onClick={isEditing ? handleSave : handleEdit}>
//           {isEditing ? 'Save' : 'Edit'}
//         </Button>
//         {!isEditing && (
//           <Button type="danger" onClick={handleDelete}>
//             Delete
//           </Button>
//         )}
//         {isEditing && (
//           <Button onClick={handleCancel}>Cancel</Button>
//         )}
//       </Card>
//     </div>
//   );
// };

// export default ProductDetail;

