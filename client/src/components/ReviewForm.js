import React, { useState, useEffect } from 'react';
import './ReviewForm.css';

const ReviewForm = () => {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState('');
  const [editReview, setEditReview] = useState({ id: null, text: '' });
  const [isEditing, setIsEditing] = useState(false);

  
  
  useEffect(() => {
    fetch('/reviews')
      .then((response) => response.json())
      .then(async (data) => {
        const reviewsWithDetails = await Promise.all(
          data.map(async (review) => {
            const userDetails = await fetchUserDetails(review.user_id);
            const productDetails = await fetchProductDetails(review.product_id);
            return { ...review, ...userDetails, ...productDetails };
          })
        );
        setReviews(reviewsWithDetails);
      });
  }, []);
  

  const fetchUserDetails = async (userId) => {
    const response = await fetch(`/users/${userId}`);
    const userData = await response.json();
    console.log('User Data:', userData);
    return { username: userData.username };
   };
   
   const fetchProductDetails = async (productId) => {
    const response = await fetch(`/products/${productId}`);
    const productData = await response.json();
    console.log('Product Data:', productData);
    return { productName: productData.name };
   };

   const handleAddReview = () => {
    if (newReview.length >= 10) {
      fetch('/reviews', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comments: newReview, user_id: 1, product_id: 1 }),
      })
        .then((response) => response.json())
        .then(async (data) => {
          const userDetails = await fetchUserDetails(data.user_id);
          const productDetails = await fetchProductDetails(data.product_id);

          const newReviewItem = {
            ...data,
            ...userDetails,
            ...productDetails,
          };

          setReviews([...reviews, newReviewItem]);
          setNewReview('');
        });
    } else {
      alert('Review must be at least 10 characters long.');
    }
   }

   const handleEditReview = (id, text) => {
    setEditReview({ id, text });
    setIsEditing(id);
   };
   

  const handleSaveReview = (id) => {
    if (editReview.text.length >= 10) {
      fetch(`/reviews/${id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comments: editReview.text }),
      })
        .then(() => {
          const updatedReviews = reviews.map((review) => {
            if (review.id === id) {
              review.comments = editReview.text;
            }
            return review;
          });
          setReviews(updatedReviews);
          setEditReview({ id: null, text: '' });
          setIsEditing(false);
        });
    } else {
      alert('Review must be at least 10 characters long.');
    }
  };
  
  const handleDeleteReview = (id) => {
    fetch(`/reviews/${id}`, {
      method: 'DELETE',
    }).then(() => {
      const updatedReviews = reviews.filter((review) => review.id !== id);
      setReviews(updatedReviews);
    });
  };

  return (
    <div className="reviews-container">
      <h2>Product Reviews</h2>
      <ul>
      {reviews.map((review) => (
 <div key={review.id} className="review-item">
   {isEditing === review.id ? (
     <input
       type="text"
       value={editReview.text}
       onChange={(e) => setEditReview({ ...editReview, text: e.target.value })}
       placeholder="Edit your review here"
     />
   ) : (
     <p className="review-text">{review.comments}</p>
   )}
   <p style={{ fontWeight: 'bold' }}>User: {review.username}</p>
   <p style={{ fontWeight: 'bold' }}>Product: {review.productName}</p>
   {isEditing === review.id ? (
     <button onClick={() => handleSaveReview(review.id)}>Save</button>
   ) : (
     <>
       <button onClick={() => handleEditReview(review.id, review.comments)}>Edit</button>
       <button onClick={() => handleDeleteReview(review.id)}>Delete</button>
     </>
   )}
 </div>
))}

      </ul>
      <div className="review-form">
        {editReview.id !== null ? (
          <>
            <input
              type="text"
              value={editReview.text}
              onChange={(e) => setEditReview({ ...editReview, text: e.target.value })}
              placeholder="Edit your review here"
            />
            <button onClick={() => handleSaveReview(editReview.id)}>Save</button>
          </>
        ) : (
          <>
            <input
              type="text"
              value={newReview}
              onChange={(e) => setNewReview(e.target.value)}
              placeholder="Leave Us A Review :)"
            />
            <button onClick={handleAddReview}>Add Review</button>
          </>
        )}
      </div>
    </div>
  )};
  
export default ReviewForm;  




// const handleAddReview = () => {
//   if (newReview.length >= 10) {
//     fetch('/reviews', {
//       method: 'POST',
//       headers: { 'Content-Type': 'application/json' },
//       body: JSON.stringify({ comments: newReview, user_id: loggedInUserId, product_id: viewedProductId }),
//     })
//       .then((response) => response.json())
//       .then((data) => {
//         setReviews([...reviews, data]);
//         setNewReview('');
//       });
//   } else {
//     alert('Review must be at least 10 characters long.');
//   }
// };
