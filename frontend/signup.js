document.addEventListener("DOMContentLoaded", () => {
    const signupForm = document.getElementById("signup-form");

    signupForm.addEventListener("submit", (e) => {
        e.preventDefault(); // Prevent form from refreshing

        const name = document.getElementById("name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value.trim();

        if (!name || !email || !password) {
            alert("All fields are required!");
            return;
        }

        // Store user data (For now, using localStorage)
        const newUser = { name, email, password };
        localStorage.setItem("user", JSON.stringify(newUser));

        alert("Signup successful! Redirecting to login...");
        window.location.href = "login.html"; // Redirect to login page
    });
});
