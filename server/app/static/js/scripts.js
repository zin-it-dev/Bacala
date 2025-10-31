window.onload = async () => {
  const response = await fetch("/stats/amount");
  const data = await response.json();

  const ctx = document.getElementById("amountChart").getContext("2d");
  new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: data.labels,
      datasets: data.datasets.map((ds) => ({
        label: "Amount",
        data: ds.data,
        backgroundColor: ds.backgroundColor,
        hoverOffset: 4
      })),
    },
  });
};
