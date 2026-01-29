import React from "react";
import BookingForm from "../../components/Forms/BookingForm";

const Booking = () => {
  return (
    <div className="grid gap-6 lg:grid-cols-2">
      <BookingForm />
      <div className="bg-white rounded-lg shadow-sm p-6">
        <h2 className="text-lg font-semibold mb-4">Upcoming Bookings</h2>
        <p className="text-gray-500 text-sm">No bookings yet.</p>
      </div>
    </div>
  );
};

export default Booking;
