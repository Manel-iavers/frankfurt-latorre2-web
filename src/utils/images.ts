/**
 * Dades per pintar una imatge PNG de public/ com a <picture> AVIF + WebP.
 *
 * Les variants les genera scripts/optimize-images.mjs, que també escriu el
 * manifest. El <picture> s'escriu a cada component (no en un component propi)
 * perquè l'<img> conservi els estils amb àmbit del component que la pinta.
 */
import manifest from '../config/images.json';

type Entry = { width: number; height: number; widths: number[] };

export function responsiveImage(src: string) {
  const entry = (manifest as Record<string, Entry>)[src];
  if (!entry) {
    throw new Error(`${src} no és al manifest: executa node scripts/optimize-images.mjs`);
  }
  const base = src.replace(/\.png$/, '');
  const srcset = (format: 'avif' | 'webp') =>
    entry.widths.map((w) => `${base}-${w}.${format} ${w}w`).join(', ');
  return {
    avif: srcset('avif'),
    webp: srcset('webp'),
    src: `${base}-${entry.widths[entry.widths.length - 1]}.webp`,
    width: entry.width,
    height: entry.height,
  };
}
