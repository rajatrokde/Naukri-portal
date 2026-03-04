<script>
const backendBase = window.location.hostname === 'localhost'
    ? 'http://localhost:30007'
    : 'http://backend-service';

document.getElementById("loginForm").addEventListener("submit", function(e) {
    e.preventDefault();
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    fetch(`${backendBase}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password })
    })
    …
});
…
</script>
