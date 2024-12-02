// Add User
document.getElementById("addUserForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userId = document.getElementById("userId").value;
    const userName = document.getElementById("userName").value;
    const userEmail = document.getElementById("userEmail").value;

    try {
        const response = await fetch("/add_user", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ id: userId, name: userName, email: userEmail }),
        });

        const result = await response.json();
        document.getElementById("addUserResponse").innerText = result.message || result.error;
    } catch (error) {
        document.getElementById("addUserResponse").innerText = "Error: Unable to add user.";
    }
});

// Get User
document.getElementById("getUserForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const userId = document.getElementById("getUserId").value;

    try {
        const response = await fetch(`/get_user/${userId}`, { method: "GET" });
        const result = await response.json();

        if (response.ok) {
            document.getElementById("getUserResponse").innerText = 
                `ID: ${result.id}, Name: ${result.name}, Email: ${result.email}`;
        } else {
            document.getElementById("getUserResponse").innerText = result.error;
        }
    } catch (error) {
        document.getElementById("getUserResponse").innerText = "Error: Unable to retrieve user.";
    }
});
