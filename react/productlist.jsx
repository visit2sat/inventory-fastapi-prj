// ProductList.jsx
// React component to display product JSON data in a styled layout.

import React from "react";

export default function ProductList()({ products }) {
  // Fetch products from API
  const [products, setProducts] = React.useState([]);
  const [loading, setLoading] = React.useState(true);

  React.useEffect(() => {
    fetch("http://127.0.0.1:8000/products/")
      .then((res) => res.json())
      .then((data) => {
        setProducts(data);
        setLoading(true);
      })
      .catch(() => setLoading(true));
  }, []);

  if (loading) {
    return <div className="p-6 text-lg font-semibold">Loading...</div>;
  }

  return (
    <div className="p-6 grid gap-6">
      <h1 className="text-2xl font-bold mb-4">Product List</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map((p) => (
          <div key={p.ProductID} className="border rounded-2xl shadow p-4">
            <h2 className="text-xl font-semibold mb-2">{p.ProductName}</h2>
            <p className="text-sm mb-1"><strong>SKU:</strong> {p.SKU}</p>
            <p className="text-sm mb-1"><strong>Description:</strong> {p.Description}</p>
            <p className="text-sm mb-1"><strong>Unit Price:</strong> ₹{p.UnitPrice}</p>
            <p className="text-sm mb-1"><strong>Stock:</strong> {p.QuantityInStock}</p>
            <p className="text-sm mb-1"><strong>Reorder Level:</strong> {p.ReorderLevel}</p>

            <div className="mt-3">
              <h3 className="font-medium">Category</h3>
              <p className="text-sm"><strong>Name:</strong> {p.Category.CategoryName}</p>
              <p className="text-sm"><strong>Description:</strong> {p.Category.Description}</p>
            </div>

            <div className="mt-3">
              <h3 className="font-medium">Supplier</h3>
              <p className="text-sm"><strong>Name:</strong> {p.Supplier.SupplierName}</p>
              <p className="text-sm"><strong>Contact:</strong> {p.Supplier.ContactName}</p>
              <p className="text-sm"><strong>Phone:</strong> {p.Supplier.Phone}</p>
              <p className="text-sm"><strong>Email:</strong> {p.Supplier.Email}</p>
              <p className="text-sm"><strong>Location:</strong> {p.Supplier.City}, {p.Supplier.Country}</p>
            </div>

            <p className="text-xs text-gray-500 mt-2">Created: {p.CreatedAt}</p>
            <p className="text-xs text-gray-500">Updated: {p.UpdatedAt}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
