//  Execute getColors() when submit button is clicked
const form = document.querySelector("#form");
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      getColors();
    });

//  Performs the POST request
function getColors() {
    const query = form.elements.query.value;
      fetch("/palette", {
        method: "POST",
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
          query: query
        })
      })
      .then((response) => response.json())
      .then(data => {
        const color_array = data;
        const container = document.querySelector(".container");
        createColorBoxes(color_array,container);
      });
}

//  Renders color boxes based on array size and contents
function createColorBoxes(color_array,parent) {
    parent.innerHTML = "";
    for(const color of color_array) {
        const div = document.createElement("div");
        div.classList.add("color");
        div.style.backgroundColor = color;
        div.style.width = `calc(100%/ ${color_array.length})`
        div.addEventListener("click", function () {
        navigator.clipboard.writeText(color);
        })
        const span = document.createElement("span");
        span.innerText = color;
        div.appendChild(span);
        parent.appendChild(div);
    }
}

