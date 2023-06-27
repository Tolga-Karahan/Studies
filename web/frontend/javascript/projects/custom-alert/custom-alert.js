function displayMessage(msgText, msgType) {
    const body = document.body;

    const panel = document.createElement("div");
    panel.setAttribute("class", "msgBox");
    body.appendChild(panel);

    const msg = document.createElement("p");
    msg.textContent = msgText;

    // Handle message type
    if (msgType === "warning") {
        msg.style.backgroundImage = "url(warning.png)";
        msg.style.backgroundColor = "red";
    } else if (msgType === "chat") {
        msg.style.backgroundImage = "url(chat.png)";
        msg.style.backgroundColor = "aqua";
    } else {
        msg.style.paddingLeft = "20px";
    }

    panel.appendChild(msg);

    const closeBtn = document.createElement("button");
    closeBtn.textContent = "x";
    panel.appendChild(closeBtn);

    closeBtn.addEventListener("click", () => 
        panel.parentNode.removeChild(panel)
    );
}

const btn = document.querySelector("button");
btn.addEventListener("click", () =>
    displayMessage("It's a custom message!", "chat")
);