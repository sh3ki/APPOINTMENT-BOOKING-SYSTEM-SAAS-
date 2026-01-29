import React from "react";

const BookingForm = () => {
  return (
    <form className="bg-white rounded-lg shadow-sm p-6 space-y-4">
      <h3 className="text-lg font-semibold">Book a Service</h3>
      <div className="grid gap-4 md:grid-cols-2">
        <input className="border rounded px-3 py-2" placeholder="Full name" />
        <input className="border rounded px-3 py-2" placeholder="Email" type="email" />
        <input className="border rounded px-3 py-2" placeholder="Phone" />
        <input className="border rounded px-3 py-2" placeholder="Service" />
      </div>
      <textarea className="border rounded px-3 py-2 w-full" placeholder="Notes" rows={3} />
      <button type="button" className="bg-brand text-white px-4 py-2 rounded">Submit</button>
    </form>
  );
};

export default BookingForm;
