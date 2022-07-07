function tableCreate(data) {
  const body = document.body;
  const table = document.createElement('table');
  const tblBody = document.createElement("tbody");
  table.style.width = '200px';
  table.style.border = '4px solid black';
  table.setAttribute("border", "2");

  const titles = data;
  for (let i = 0; i < titles.length; i++) {
    const row = document.createElement("tr");
    const cell = document.createElement("td");
    const cellText = document.createTextNode(titles[i]);
    cell.appendChild(cellText);
    row.appendChild(cell);
    tblBody.appendChild(row)
  }

  table.appendChild(tblBody)
  body.appendChild(table)
}

fetch('http://localhost:5000/en')
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    tableCreate(data);
  });