import React from "react";

const Sidebar = () => {
  return (
    <aside className="bg-white rounded-lg shadow-sm p-4">
      <h3 className="text-sm font-semibold text-gray-700 mb-3">Quick Actions</h3>
      <ul className="text-sm space-y-2">
        <li>Create service</li>
        <li>Add availability</li>
        <li>View reports</li>
      </ul>
    </aside>
  );
};

export default Sidebar;
