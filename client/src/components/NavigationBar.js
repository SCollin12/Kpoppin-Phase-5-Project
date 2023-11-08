import { useHistory } from 'react-router-dom';
import { useAuth } from './AuthContext';
import { Link } from 'react-router-dom';

const NavigationBar = ({ className }) => {
  const { setIsUserLoggedIn } = useAuth();
  const history = useHistory();

  const handleLogout = () => {
    fetch('/logout', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        if (response.status === 204) {
          // Update the authentication status to logged out
          setIsUserLoggedIn(false);

          history.push('/'); // Redirect to the homepage or the startup page
        } else {
          console.error('Logout failed');
        }
      })
      .catch((error) => {
        console.error('Logout failed', error);
      });
  };

  return (
    <nav className={className}>
      <ul>
        <li>
          <Link to="/reviews">Reviews</Link>
        </li>
        <li>
          <Link to="/products">Products</Link>
        </li>
        <li>
          <Link to="/orders">Orders</Link>
        </li>
        <li>
          <Link to="/signup-login">Sign Up / Login</Link>
        </li>
        <li>
          {/* Display the logout button only when the user is logged in */}
          {setIsUserLoggedIn && <button onClick={handleLogout}>Logout</button>}
        </li>
      </ul>
    </nav>
  );
};

export default NavigationBar;


