const twitter = document.querySelector(".twitter");
const whatsapp = document.querySelector(".whatsapp");
const telegram = document.querySelector(".telegram");
const facebook = document.querySelector(".facebook");

const pageUrl = location.href;
const msg = "This is my business QR code, open, scan and shop";

const whatsappApi = `https://wa.me/?text=${pageUrl}. ${msg}`;
const twitterApi = ` https://twitter.com/intent/tweet?text=${pageUrl}. ${msg}`;
const telegramApi = `https://t.me/share/url?url=${pageUrl}&text=${msg}`;
//const facebookApi = `https://www.facebook.com/sharer/sharer.php?u=${pageUrl}. ${msg}`
const facebookApi = `https://www.facebook.com/sharer/sharer.php?u=www.google.com`;

whatsapp.addEventListener("click", () => {
  window.open((ulr = whatsappApi), (target = "blank"));
});

twitter.addEventListener("click", () => {
  window.open((ulr = twitterApi), (target = "blank"));
});

telegram.addEventListener("click", () => {
  window.open((ulr = telegramApi), (target = "blank"));
});

facebook.addEventListener("click", () => {
  window.open((ulr = facebookApi), (target = "blank"));
});
