function selectDestination(destination) {
    document.getElementById("destination").value = destination;
    document.getElementById("booking").scrollIntoView({ behavior: "smooth" });
}

document.getElementById("bookingForm").addEventListener("submit", async function(event) {
    event.preventDefault();

    const result = document.getElementById("bookingResult");
    const formData = new FormData(this);
    result.textContent = "Processing booking...";

    try {
        const response = await fetch("/book", { method: "POST", body: formData });
        const data = await response.json();

        if (!response.ok) {
            result.textContent = data.message || "Unable to complete booking.";
            result.style.color = "#c0392b";
            return;
        }

        result.textContent = `Booking submitted successfully! Your booking ID is ${data.booking_id}.`;
        result.style.color = "#168a4a";
        this.reset();

    } catch (error) {
        result.textContent = "Server error. Please try again.";
        result.style.color = "#c0392b";
    }
});
