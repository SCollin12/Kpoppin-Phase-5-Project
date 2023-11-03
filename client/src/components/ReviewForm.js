import React, { useState, useEffect } from 'react';

const ReviewForm = () => {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState('');
  const [editReview, setEditReview] = useState({ id: null, text: '' });

  useEffect(() => {
    fetch('/reviews')
      .then((response) => response.json())
      .then((data) => setReviews(data));
  }, []);

  const handleAddReview = () => {
    fetch('/reviews', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ comments: newReview, user_id: 1, product_id: 1 }),
    })
      .then((response) => response.json())
      .then((data) => {
        setReviews([...reviews, data]);
        setNewReview('');
      });
  };

  const handleEditReview = (id, text) => {
    setEditReview({ id, text });
  };

  const handleSaveReview = (id) => {
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
      });
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
    <div>
      <h2>Reviews</h2>
      <ul>
        {reviews.map((review) => (
          <li key={review.id}>
            {review.id === editReview.id ? (
              <div>
                <input
                  type="text"
                  value={editReview.text}
                  onChange={(e) => setEditReview({ ...editReview, text: e.target.value })}
                />
                <button onClick={() => handleSaveReview(review.id)}>Save</button>
              </div>
            ) : (
              <span>{review.comments}</span>
            )}
            <button onClick={() => handleEditReview(review.id, review.comments)}>Edit</button>
            <button onClick={() => handleDeleteReview(review.id)}>Delete</button>
          </li>
        ))}
      </ul>
      <div>
        <input
          type="text"
          value={newReview}
          onChange={(e) => setNewReview(e.target.value)}
          placeholder="Write a new review"
        />
        <button onClick={handleAddReview}>Add Review</button>
      </div>
    </div>
  );
};

export default ReviewForm;

