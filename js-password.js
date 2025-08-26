// password-generator.js

function generatePassword(length = 12, options = {}) {
  const huruf = "abcdefghijklmnopqrstuvwxyz";
  const hurufBesar = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  const angka = "0123456789";

  let semua = "";

  if (options.huruf) semua += huruf;
  if (options.besar) semua += hurufBesar;
  if (options.angka) semua += angka;

  // kalau user tidak pilih apapun, default pakai semua
  if (!semua) semua = huruf + hurufBesar + angka;

  let password = "";
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * semua.length);
    password += semua[randomIndex];
  }
  return password;
}

// Ambil argumen dari terminal
const args = process.argv.slice(2);
let panjang = 12;
let options = { huruf: false, besar: false, angka: false };

if (args.length > 0) {
  const parsed = parseInt(args[0], 10);
  if (!isNaN(parsed) && parsed > 0) {
    panjang = parsed;
  }
  if (args.includes("--huruf")) options.huruf = true;
  if (args.includes("--besar")) options.besar = true;
  if (args.includes("--angka")) options.angka = true;
}

console.log("Panjang password:", panjang);
console.log("Password kamu :", generatePassword(panjang, options));
