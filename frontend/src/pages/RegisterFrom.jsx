import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";
import "../styles/form.css";
import api from "../api";

const RegisterForm = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email,setEmail] = useState("")
  const [firstName,setFirstName] = useState("")
  const [lastName,setLastName] = useState("")
  const [mobile,setMobile] = useState("")
  const [address,setAddress] = useState("")
  const [pincode,setPincode] = useState("")
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await api.post('/api/user/register', { username, email, password, first_name:firstName, last_name:lastName ,mobile ,address ,pin_code:pincode });
      if(res.status==201){
        navigate("/login");
      }else{
        alert('Error while registering user')
      }
      
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };
  return (
    <form onSubmit={handleSubmit} className="form-container">
      <h1>Register</h1>
      <input
        className="form-input"
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        placeholder="Username"
      />
      <input
        className="form-input"
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="email"
      />
      <input
        className="form-input"
        type="text"
        value={firstName}
        onChange={(e) => setFirstName(e.target.value)}
        placeholder="first name"
      />
      <input
        className="form-input"
        type="text"
        value={lastName}
        onChange={(e) => setLastName(e.target.value)}
        placeholder="last name"
      />
      <input
        className="form-input"
        type="text"
        value={mobile}
        onChange={(e) => setMobile(e.target.value)}
        placeholder="phone number"
      />
      <input
        className="form-input"
        type="text"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
        placeholder="address"
      />
      <input
        className="form-input"
        type="text"
        value={pincode}
        onChange={(e) => setPincode(e.target.value)}
        placeholder="pin code"
      />
      <input
        className="form-input"
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
      />
      <button className="form-button" type="submit">
        Login
      </button>
    </form>
  );
};

export default RegisterForm;
