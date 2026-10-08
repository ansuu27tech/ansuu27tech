# Asset Sources & Image Injection

This repository contains SVGs designed for the GitHub profile. 
As per the requirements, the SVGs are fully self-contained and safe for GitHub.

## Adding your custom images

Since the profile requires `id.png` and `right_pointing.png` to be embedded directly via Base64 (to avoid external network dependencies), you need to inject your images into the SVGs.

### Manual Injection
1. Convert your `id.png` and `right_pointing.png` to Base64 (using a tool like [Base64 Image Encoder](https://www.base64-image.de/)).
2. Open `assets/hero.svg`, `assets/id-dashboard.svg`, and `assets/connect.svg` in a text editor.
3. Find the `<image ... id="hero-avatar">`, `<image ... id="id-avatar">`, or `<image ... id="connect-image">` tag.
4. Replace the `href="data:image/png;base64,..."` value with your new Base64 string.

### Automated Injection (Node.js)
If you have Node.js installed, you can use a simple script to inject the images automatically.

Place your actual images in the `images/` directory:
- `images/id.png`
- `images/right_pointing.png`

Create a script `inject.js`:
```javascript
const fs = require('fs');

const idBase64 = 'data:image/png;base64,' + fs.readFileSync('./images/id.png', 'base64');
const rpBase64 = 'data:image/png;base64,' + fs.readFileSync('./images/right_pointing.png', 'base64');

['hero.svg', 'id-dashboard.svg'].forEach(file => {
  let content = fs.readFileSync(`./assets/${file}`, 'utf-8');
  content = content.replace(/href="data:image\/png;base64,[^"]*"/g, `href="${idBase64}"`);
  fs.writeFileSync(`./assets/${file}`, content);
});

let connect = fs.readFileSync('./assets/connect.svg', 'utf-8');
connect = connect.replace(/href="data:image\/png;base64,[^"]*"/g, `href="${rpBase64}"`);
fs.writeFileSync('./assets/connect.svg', connect);

console.log('Images successfully injected!');
```
Run `node inject.js` and the SVGs will be updated automatically!

## Fonts
The fonts `Inter` and `JetBrains Mono` are referenced via CSS. If strict offline/no-network SVGs are required, you must base64 encode the `.woff2` files and embed them in the `<style>` block using `@font-face`.
