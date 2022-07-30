### From scratch


1. Install what we know we need: Svelte and Vite [^1]

```
npm install svelte vite @sveltejs/kit @sveltejs/adapter-auto --save-dev
```

2. Add `svelte.config.js`

```javascript
import adapter from '@sveltejs/adapter-auto';

const config = {
	kit: {
		adapter: adapter()
	}
};
export default config
```

2. Add `vite.config.js`

```javascript
import { sveltekit } from '@sveltejs/kit/vite';

const config = {plugins: [sveltekit()]};
export default config

```

4. Add `scripts` and *type: module* `package.json` 

```json
"scripts": {
    "dev": "vite --host 0.0.0.0 --port 3001",
    "build": "vite build"
},
"type": "module"
```

5. 🥳 Add an `app.html` file and a `routes` folder and get goin' 


[^1]: Svelte: (of a person) slender and elegant. Try and work that into a
  conversation today.

