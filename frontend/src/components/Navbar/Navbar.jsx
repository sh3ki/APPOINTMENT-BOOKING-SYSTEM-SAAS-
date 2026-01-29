import React from "react";
import { Link, NavLink } from "react-router-dom";

const Navbar = () => {
  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-6xl mx-auto px-4 py-4 flex items-center justify-between">
        <Link to="/" className="text-xl font-semibold text-brand">Appointment SaaS</Link>
        <nav className="flex items-center gap-4 text-sm">
          <NavLink to="/" className="hover:text-brand">Dashboard</NavLink>
          <NavLink to="/booking" className="hover:text-brand">Bookings</NavLink>
          <NavLink to="/admin" className="hover:text-brand">Admin</NavLink>
          <NavLink to="/login" className="text-brand font-medium">Login</NavLink>
        </nav>
      </div>
    </header>
  );
};

export default Navbar;
