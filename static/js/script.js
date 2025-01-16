document.addEventListener("DOMContentLoaded", () => {
    async function submitSignup(event) {
        event.preventDefault(); // Prevent the default form submission

        const form = document.getElementById("signup-form");
        const formData = new FormData(form);

        const payload = {
            name: formData.get("name"),
            email: formData.get("email"),
            password: formData.get("password"),
        };

        try {
            const response = await fetch("/users/signup", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload), // Send data as JSON
            });

            if (response.ok) {
                alert("Account created successfully!");
                window.location.href = "/login";
            } else {
                const error = await response.json();
                alert(error.error || "Signup failed!");
            }
        } catch (err) {
            alert("An error occurred. Please try again.");
        }
    }

    async function submitLogin(event) {
        event.preventDefault(); // Prevent the default form submission

        const form = document.getElementById("login-form");
        const formData = new FormData(form);

        const payload = {
            email: formData.get("email"),
            password: formData.get("password"),
        };

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(payload), // Send data as JSON
            });

            if (response.ok) {
                alert("Login successful!");
                window.location.href = "/profile";
            } else {
                const error = await response.json();
                alert(error.error || "Login failed!");
            }
        } catch (err) {
            alert("An error occurred. Please try again.");
        }
    }

    const signupForm = document.getElementById("signup-form");
    if (signupForm) {
        signupForm.onsubmit = submitSignup;
    }

    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.onsubmit = submitLogin;
    }
});