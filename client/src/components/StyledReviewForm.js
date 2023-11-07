import React, { useState, useEffect } from 'react';
import { Input, Button, List, Avatar, Space } from 'antd';
import 'antd/dist/antd.css'; // Import Ant Design CSS
import './StyledReviewForm.css'; // You can create your custom CSS for additional styling

const StyledReviewForm = () => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    // Fetch review data from your API
    fetch('/reviews')
      .then((response) => response.json())
      .then((data) => setReviews(data));
  }, []);

  return (
    <div className="styled-review-form">
      <h2>Reviews</h2>
      <div>
        <Input type="text" placeholder="Leave Us A Review :)" />
        <Button type="primary">Add Review</Button>
      </div>
      <div>
        {/* Display the list of reviews using Ant Design List component */}
        <List
          itemLayout="vertical"
          size="large"
          dataSource={reviews}
          renderItem={(review) => (
            <List.Item
              key={review.id}
              actions={[
                <Space>
                  <span>{review.comments.length} comments</span>
                  {/* Add more actions if needed */}
                </Space>
              ]}
            >
              <List.Item.Meta
                avatar={<Avatar src={review.user.avatar} />}
                title={review.user.username}
                description={`Reviewed a product: ${review.product.name}`}
              />
              <div>{review.comments}</div>
            </List.Item>
          )}
        />
      </div>
    </div>
  );
};

export default StyledReviewForm;

