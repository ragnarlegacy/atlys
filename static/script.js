const apiBaseUrl = "http://192.168.31.93:9000"; // Replace with the backend API URL

document.getElementById("userForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;

  try {
    const response = await fetch(`${apiBaseUrl}/users`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, email }),
    });

    if (response.ok) {
      alert("User added successfully!");
      document.getElementById("userForm").reset();
    } else {
      const error = await response.json();
      alert(`Error: ${error.message || "Unable to add user"}`);
    }
  } catch (error) {
    console.error("Error adding user:", error);
    alert("An error occurred while adding the user.");
  }
});

document.getElementById("fetchUsers").addEventListener("click", async () => {
  try {
    const response = await fetch(`${apiBaseUrl}/users`);

    if (response.ok) {
      const users = await response.json();
      const tbody = document.getElementById("usersTable").querySelector("tbody");
      tbody.innerHTML = ""; // Clear previous table data

      users.forEach((user) => {
        const row = document.createElement("tr");
        row.innerHTML = `
          <td>${user.id}</td>
          <td>${user.name}</td>
          <td>${user.email}</td>
        `;
        tbody.appendChild(row);
      });
    } else {
      const error = await response.json();
      alert(`Error: ${error.message || "Unable to fetch users"}`);
    }
  } catch (error) {
    console.error("Error fetching users:", error);
    alert("An error occurred while fetching the users.");
  }
});
