# Fonda Vercel deployment


---

## Dev:

### Minifying CSS:

- [Use me](https://codebeautify.org/css-beautify-minify#)
### JS:

- Access errors:
    sometimes you get access not granted
    ```zsh
    chmod +x /Users/user/Library/Caches/com.vercel.fun/runtimes/python3/bootstrap  
    ```

- Terser:
    compress, mangile & .js.map as well.
    ```zsh
    terser original_libs/fonda-sleek.js --compress --mangle --comments "false" --output "static/my-fonda-lib-v1.js" --source-map "url='static/my-fonda-lib-v1.js.map',content='inline'"  
    ```

### Caches
you can invalidate cache just by adding a ?v=2 whatever numb to end of your js/css file to force fetching static files.
sadly, this didn't work:
- invalidating cache changing name file -> one works for me


### CDN:

- Use Github-CDN + JSDeliver:
    - js
    `https://cdn.jsdelivr.net/gh/MoElaSec/github-cdn/js/my-talib-lib-v6.js`

    - CSS
    `https://cdn.jsdelivr.net/gh/MoElaSec/github-cdn/css/talib-v4.css`

### Pylint:

```python3
pylint app.py
```