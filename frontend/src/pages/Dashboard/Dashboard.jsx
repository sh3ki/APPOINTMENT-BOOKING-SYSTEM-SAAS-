import React from "react";
import BookingCalendar from "../../components/BookingCalendar/BookingCalendar";
import Sidebar from "../../components/Sidebar/Sidebar";

const Dashboard = () => {
  return (
    <div className="grid gap-6 lg:grid-cols-[2fr,1fr]">
      <BookingCalendar />
      <Sidebar />
    </div>
  );
};

export default Dashboard;
