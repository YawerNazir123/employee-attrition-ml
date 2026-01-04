const canvas = document.getElementById("impactChart");

if (canvas) {
    const ctx = canvas.getContext("2d");

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: [
                "Job Satisfaction",
                "Work Life Balance",
                "Income",
                "Experience"
            ],
            datasets: [{
                label: "Impact on Attrition",
                data: [85, 75, 65, 60],
                backgroundColor: [
                    "#60a5fa",
                    "#34d399",
                    "#fbbf24",
                    "#f87171"
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    labels: { color: "#e5e7eb" }
                }
            },
            scales: {
                x: { ticks: { color: "#e5e7eb" } },
                y: { ticks: { color: "#e5e7eb" } }
            }
        }
    });
}
