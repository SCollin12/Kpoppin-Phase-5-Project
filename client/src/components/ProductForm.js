import React from 'react';
import { Form, Input, Button, Select, DatePicker } from 'antd';

const ProductForm = (props) => {
    const [form] = Form.useForm();
  
    const handleFormSubmit = async () => {
      const productForm = form.getFieldsValue();
      console.log('Sending data to the server: ', productForm);
  
      fetch('/products', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(productForm),
      })
      .then((res) => {
        if (res.status === 201) {
          console.log('Response status:', res.status);
          res.json().then((newProduct) => {
            props.onProductAdded(newProduct);
          });
        } else {
          console.error('Product addition failed');
        }
      })
      .catch((error) => {
        console.error('Error adding product', error);
      });
  
      // Reset the form fields
      form.resetFields();
    };
  
  

  return (
    <div>
      <h2>Add Product To Inventory *Admin Use Only*</h2>
      <Form form={form} onFinish={handleFormSubmit}>
        <Form.Item label="Name" name="name" rules={[{ required: true, message: 'Please input the product name!' }]}>
          <Input placeholder="Product Name" />
        </Form.Item>
        <Form.Item label="Description" name="description" rules={[{ required: true, message: 'Please input the product description!' }]}>
          <Input placeholder="Product Description" />
        </Form.Item>
        <Form.Item label="Price" name="price" rules={[{ required: true, message: 'Please input the product price!' }]}>
          <Input placeholder="Product Price" />
        </Form.Item>
        <Form.Item label="Release Date" name="release_date" rules={[{ required: true, message: 'Please input the product release date!' }]}>
          <DatePicker placeholder="Product Release Date" />
        </Form.Item>
        <Form.Item label="Image URL" name="image_url" rules={[{ required: true, message: 'Please input the product image URL!' }]}>
          <Input placeholder="Product Image URL" />
        </Form.Item>
        <Form.Item label="Type" name="type" rules={[{ required: true, message: 'Please select the product type!' }]}>
          <Select placeholder="Product Type">
            <Select.Option value="kpop">K-pop</Select.Option>
            <Select.Option value="anime">Anime</Select.Option>
          </Select>
        </Form.Item>
        <Form.Item>
          <Button type="primary" htmlType="submit">Add Product</Button>
        </Form.Item>
      </Form>
    </div>
  );
};

export default ProductForm;

