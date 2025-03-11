document.addEventListener("DOMContentLoaded", () => {
    const loginForm = document.getElementById("login-form");

    loginForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent form from refreshing the page

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        // Simulated user data (replace this with real database authentication)
        const users = [
            { email: "user@example.com", password: "password123" },
            { email: "test@netflixclone.com", password: "netflix123" }
        ];

        const user = users.find(u => u.email === email && u.password === password);

        if (user) {
            alert("Login successful!");
            localStorage.setItem("user", JSON.stringify(user)); // Store user session
            window.location.href = "../index.html"; // Redirect to homepage
        } else {
            alert("Invalid email or password. Please try again.");
        }
    });
});
