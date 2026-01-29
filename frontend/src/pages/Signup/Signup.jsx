import React from "react";
import { Link } from "react-router-dom";

const Signup = () => {
  return (
    <div className="max-w-md mx-auto bg-white rounded-lg shadow-sm p-6">
      <h1 className="text-xl font-semibold mb-4">Create account</h1>
      <div className="space-y-3">
        <input className="border rounded w-full px-3 py-2" placeholder="Name" />
        <input className="border rounded w-full px-3 py-2" placeholder="Email" />
        <input className="border rounded w-full px-3 py-2" placeholder="Password" type="password" />
        <button className="bg-brand text-white w-full py-2 rounded">Create account</button>
      </div>
      <p className="text-sm mt-4">Already have an account? <Link className="text-brand" to="/login">Login</Link></p>
    </div>
  );
};

export default Signup;
