import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <div className="navbar bg-gray-800 text-white p-4">
      <Link className="px-2 py-1 hover:bg-gray-700" to="/catalogue">Catalogue</Link>
      <Link className="px-2 py-1 hover:bg-gray-700" to="/auctions">Auctions</Link>
      <Link className="px-2 py-1 hover:bg-gray-700" to="/vouchers">Vouchers</Link>
      <Link className="px-2 py-1 hover:bg-gray-700" to="/profile">Profile</Link>
      <Link className="px-2 py-1 hover:bg-gray-700" to="/cart">Cart</Link>
      <Link className="px-2 py-1 hover:bg-gray-700" to="/login">Login/Sign Up</Link>
    </div>
  );
}

export default Navbar;
