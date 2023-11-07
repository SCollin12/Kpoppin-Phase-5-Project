import React, { useState } from 'react';

const ProductForm = () => {
  const [productForm, setProductForm] = useState({
    name: '',
    description: '',
    price: '',
    release_date: '',
    image_url: '',
    type: '',
  });

  const handleFormChange = (name, value) => {
    setProductForm((prevProductForm) => ({
      ...prevProductForm,
      [name]: value,
    }));
  };
  
  const handleFormSubmit = (event) => {
    console.log('Sending data to the server: ', productForm);
    event.preventDefault();


    // Send a POST request to add the product to the database
    fetch('/products', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(productForm),
    })
      .then((res) => {
        if (res.status === 201) {
            console.log('Response status:', res.status);
          // Product added successfully, you can perform further actions here
        } else {
            console.error('Product addition failed');
          // Handle errors
        }
      })
      .catch((error) => {
        console.error('Error adding product', error);
      });
  };

  return (
    <div>
      <h2>Add Product</h2>
      <form onSubmit={handleFormSubmit}>
        <div>
          <label htmlFor="name">Name</label>
          <input
            type="text"
            name="name"
            value={productForm.name}
            onChange={(e) => handleFormChange('name', e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="description">Description</label>
          <input
            type="text"
            name="description"
            value={productForm.description}
            onChange={(e) => handleFormChange('description', e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="price">Price</label>
          <input
            type="number"
            name="price"
            value={productForm.price}
            onChange={(e) => handleFormChange('price', e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="release_date">Release Date</label>
          <input
            type="date"
            name="release_date"
            value={productForm.release_date}
            onChange={(e) => handleFormChange('release_date', e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="image_url">Image URL</label>
          <input
            type="text"
            name="image_url"
            value={productForm.image_url}
            onChange={(e) => handleFormChange('image_url', e.target.value)}
          />
        </div>
        <div>
          <label htmlFor="type">Type</label>
          <select
            name="type"
            value={productForm.type}
            onChange={(e) => handleFormChange('type', e.target.value)}
          >
            <option value="kpop">K-pop</option>
            <option value="anime">Anime</option>
          </select>
        </div>
        <div>
          <button type="submit">Add Product</button>
        </div>
      </form>
    </div>
  );
};

export default ProductForm;
