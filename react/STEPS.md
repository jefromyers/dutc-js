### From scratch


1. Install what we know we need: React & React-dom
    - `npm install react react-dom`

2. Install dev dependencies [^1]
    - `npm install vite @vitejs/plugin-react --save-dev`

3. Add `vite.config.js`
    - ```
    import { defineConfig } from 'vite'
    import react from '@vitejs/plugin-react'

    export default defineConfig({ plugins: [react()] })
    ```

4. Add `scripts` and whatever to our `package.json` [^2]
    - ```
    "scripts": {
        "dev": "vite --host 0.0.0.0 --port 3000",
        "build": "vite build",
    }
    ```

5. 🥳 Add an `html` file and a `js` file and get goin' 


[^1]: Grumble to yourself about how you don't have some version of node you
  should have. Try to update it with `brew` and then grumble to yourself again
  about how much you dislike `brew`. Switch to your linux machine and bask in
  the peaceful tranquility.

[^2]: Add whatever else we need here, too. `name`, `version`, etc... but make
  sure you don't add that last comma or JSON will punish you. 
