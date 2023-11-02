import { useState } from "react";
import { useNavigate } from 'react-router-dom';

function Signup() {
    const initialValue = {
        username: '',
        email: '',
        password: '',
    };
    
    const navigate = useNavigate();
    const [userExists, setUserExists] = useState(false);
    const [validationError, setValidationError] = useState(false);
    const [signupForm, setSignupForm] = useState(initialValue);

    function handleSignupChange(e) {
        const name = e.target.name;
        const value = e.target.value;
        setSignupForm({
            ...signupForm, 
            [name]: value
        });
    }

    function handleSignupSubmit(e) {
        e.preventDefault();
        fetch('/signup', {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify(signupForm)
        })
        .then((res) => {
            if (res.status === 201){
                return res.json();
            } else if (res.status === 500){
                setUserExists(true);
                setValidationError(false);
                console.error('Username or email already exists');
                setSignupForm({
                    ...signupForm, 
                    username: '',
                    email: '', // Clear the email field
                });
                return Promise.reject('Username or email already exists');
            } else if(res.status === 400){
                setUserExists(false);
                setValidationError(true);
                console.error('Username, email, and password must be present');
                return Promise.reject('Username, email, and password must be present');
            }
        })
        .then((data) => {
            navigate('/home');
        })
        .catch((error) => console.error('Error', error));
    }

    const warningStyles = {
        color: "red",
        marginTop: "-10px",
        marginBottom: "10px",
        textAlign: "center",
    };

    const warningStyles2 = {
        color: "red",
        marginTop: "-10px",
        marginBottom: "10px",
        width: "90%",
        textAlign: "center",
    };

    const signupDiv = (
        <div className="signup-form-container">
            <form className="signup-form" onSubmit={handleSignupSubmit}>
                <input type="text" autoComplete='off' placeholder="Username" onChange={handleSignupChange} name='username' value ={signupForm.username}  />
                <input type="text" autoComplete='off' placeholder="Email" onChange={handleSignupChange} name='email' value ={signupForm.email}  />
                {userExists ? <p style={warningStyles}>Username or email already exists, please try again!</p> : null}
                <input type="password" autoComplete='off' placeholder="Password" onChange={handleSignupChange} name='password' value={signupForm.password} />
                {validationError ? <p style={warningStyles2}>Username, email, and password must be present, please try again!</p> : null}
                <button className="login-signup-submit">Sign Up</button>
            </form>
            <div className="login-signup-toggle" onClick={() => {navigate('/')}}>Login</div>
        </div>
    );

    return (
        <div className="login-signup-page">
            <div className="greeting-div">
                <h1 className="greeting"><span className="fit">Fit</span><span className="connect">Connect</span></h1>
                <h3 className="sub-greeting">Remember, every small step leads to a big change. Let's embark on this journey together and make fitness a part of your lifestyle.</h3>
            </div>
            {signupDiv}
        </div>
    );
}

export default Signup;

