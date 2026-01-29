import React from "react";

const Admin = () => {
  return (
    <div className="bg-white rounded-lg shadow-sm p-6">
      <h1 className="text-xl font-semibold mb-4">Admin Dashboard</h1>
      <div className="grid gap-4 md:grid-cols-3">
        <div className="p-4 rounded bg-gray-50">
          <p className="text-sm text-gray-500">Bookings</p>
          <p className="text-2xl font-semibold">0</p>
        </div>
        <div className="p-4 rounded bg-gray-50">
          <p className="text-sm text-gray-500">Revenue</p>
          <p className="text-2xl font-semibold">$0</p>
        </div>
        <div className="p-4 rounded bg-gray-50">
          <p className="text-sm text-gray-500">Active Users</p>
          <p className="text-2xl font-semibold">0</p>
        </div>
      </div>
    </div>
  );
};

export default Admin;
