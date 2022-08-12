const qrcodeEl = document.querySelector("#qrcode");
const textEl = document.querySelector("#text");
const generateEl = document.querySelector("#generate");
const widthEl = document.querySelector("#width");
const heightEl = document.querySelector("#height");
const darkEl = document.querySelector("#dark");
const lightEl = document.querySelector("#light");
const downloadEl = document.querySelector("#download");
const downloaddEl = document.querySelector("#downloadd");
const downloadddEl = document.querySelector("#downloaddd");

generateEl.addEventListener("click", generate);

function generate() {
  qrcodeEl.innerHTML = ``;
  new QRCode(qrcodeEl, {
    text: textEl.value,
    width: widthEl.value,
    height: heightEl.value,
    colorDark: darkEl.value,
    colorLight: lightEl.value,
  });

  download();
}

function download() {
  const canvasEl = qrcodeEl.querySelector("canvas");
  let data = canvasEl.toDataURL("image/png");

  downloadEl.setAttribute("href", data);
  downloadEl.style.display = "inline-block";
  downloaddEl.setAttribute("href", data);
  downloaddEl.style.display = "inline-block";
  downloadddEl.setAttribute("href", data);
  downloadddEl.style.display = "inline-block";
}
