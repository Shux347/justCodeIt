import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';  // Assuming you have a Navbar component
import LoginSignupPage from './pages/LoginSignupPage';
import CataloguePage from './pages/CataloguePage';
import AuctionsPage from './pages/AuctionsPage';
import VouchersPage from './pages/VouchersPage';
import ProfilePage from './pages/ProfilePage';
import CartCheckoutPage from './pages/CartCheckoutPage';
import './App.css';

function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/login" element={<LoginSignupPage />} />
        <Route path="/catalogue" element={<CataloguePage />} />
        <Route path="/auctions" element={<AuctionsPage />} />
        <Route path="/vouchers" element={<VouchersPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/cart" element={<CartCheckoutPage />} />
        <Route path="/" element={<CataloguePage />} />
      </Routes>
    </Router>
  );
}

export default App;
