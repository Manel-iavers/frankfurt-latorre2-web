// Genera variants AVIF i WebP responsives de les imatges PNG del web.
//
// Ús: node scripts/optimize-images.mjs
//
// Les PNG originals es queden a public/ com a font: les variants es poden
// regenerar amb una altra qualitat sense perdre res. El manifest que escriu a
// src/config/images.json el llegeix src/utils/images.ts per
// saber quines amplades hi ha i la proporció real de cada imatge.
import sharp from 'sharp';
import { stat, writeFile } from 'node:fs/promises';
import path from 'node:path';

const root = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const publicDir = path.join(root, 'public');

// Amplades segons la mida màxima a què es mostra cada imatge (CSS) ×2 per a
// pantalles retina, sense passar mai de l'original.
const products = [
  'bacoWeb', 'bikiniWeb', 'bratwurstWeb', 'burguerWeb', 'cervelaweb', 'formatgeWeb',
  'frankfurtweb', 'llomWeb', 'malaguenyaWeb', 'pikantWeb', 'pinxoWeb', 'pollastreWeb',
  'truitaWeb', 'xoriWeb',
].map((name) => ({ src: `/images/${name}.png`, widths: [400, 800] }));

const images = [
  ...products,
  { src: '/ninotfrankfurtWeb.png', widths: [400, 800] }, // mascota del hero, ≤400px
  { src: '/logo1Web.png', widths: [480, 960, 1536] },     // fons del hero, ≤800px
  { src: '/faviconWeb.png', widths: [100] },              // logo de capçalera i peu, 50px
];

const QUALITY = { avif: 55, webp: 78 };
const manifest = {};
let written = 0;
let before = 0;
let after = 0;

for (const { src, widths } of images) {
  const input = path.join(publicDir, src);
  const meta = await sharp(input).metadata();
  before += (await stat(input)).size;
  const base = src.replace(/\.png$/, '');
  const usable = widths.filter((w) => w <= meta.width);

  for (const w of usable) {
    for (const format of ['avif', 'webp']) {
      const out = path.join(publicDir, `${base}-${w}.${format}`);
      const info = await sharp(input)
        .resize({ width: w, withoutEnlargement: true })
        [format]({ quality: QUALITY[format], effort: 6 })
        .toFile(out);
      after += info.size;
      written += 1;
    }
  }
  manifest[src] = { width: meta.width, height: meta.height, widths: usable };
}

await writeFile(path.join(root, 'src/config/images.json'), JSON.stringify(manifest, null, 2) + '\n');

console.log(`${written} variants escrites a public/ per a ${images.length} imatges`);
console.log(`Manifest: src/config/images.json (${Object.keys(manifest).length} entrades)`);
console.log(`PNG originals: ${(before / 1024).toFixed(0)} KiB · totes les variants: ${(after / 1024).toFixed(0)} KiB`);
if (written === 0) {
  console.error('No s\'ha escrit cap variant');
  process.exit(1);
}
