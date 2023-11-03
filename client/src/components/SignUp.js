import React, { useState } from 'react';

const SignUp = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
  });

  const [signupSuccess, setSignupSuccess] = useState(null);
  const [signupError, setSignupError] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch('/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.status === 201) {
        setSignupSuccess('Signup successful. You can now log in.');
        setSignupError(null);
        // Clear the form data
        setFormData({
          username: '',
          email: '',
          password: '',
        });
      } else {
        const data = await response.json();
        setSignupError(data.error);
        setSignupSuccess(null);
      }
    } catch (error) {
      console.error('Error:', error);
      setSignupError('An error occurred during signup.');
      setSignupSuccess(null);
    }
  };

  return (
    <div>
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
          placeholder="Username"
        />
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
          placeholder="Email"
        />
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
          placeholder="Password"
        />
        <button type="submit">Sign Up</button>
      </form>
      {signupSuccess && <p className="success-message">{signupSuccess}</p>}
      {signupError && <p className="error-message">{signupError}</p>}
    </div>
  );
};

export default SignUp;





