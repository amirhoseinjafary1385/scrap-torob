window.alert(" خیلی خوش آمدید کاربر محترم ..");

const iconElement = document.getElementById("pop");
const body = document.body;

iconElement.addEventListener("click", () => {
    body.classList.toggle('dark-mode');
    if(body.classList.contains('dark-mode')) {
        iconElement.setAttribute("name", "sun");
    }else {
        // آیکون زمانی که در حالت روشن است
        iconElement.setAttribute("name", "popsicle");
    }
});

const style = document.createElement("style");
style.innerHTML = `
    body {
    transition: background-color 0.6s ease, color 0.6s ease;
    }

    body.dark-mode {
        background-color: #121212;
        color: #ffffff;
        transition: background-color 0.6s ease;
    }

    body.dark-mode .box-icon {
        filter: invert(1);  // معکوس کردن رنگ آیکون
    }

    .box-icon {
        transition: filter 0.5s ease; /* افزودن transition به آیکون */
    }
`;
document.head.appendChild(style);