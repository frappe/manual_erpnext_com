## ERPNext Manual

manual.erpnext.com

### To Contribute

You will need to fork this repository and send pull requests of your changes

### Install

Install Frappe Bench: https://github.com/frappe/bench

Step 1. Create a new site on the bench

```
$ bench new-site manual.erpnext.com
```

Step 2. Then install the app in the bench

```
$ bench get-app frappe_theme git@github.com:frappe/frappe_theme
$ bench get-app manual_erpnext_com git@github.com:frappe/manual_erpnext_com
```

Step 3: Then install the app in the site

```
$ bench --site manual.erpnext.com install-app frappe_theme
$ bench --site manual.erpnext.com install-app manual_erpnext_com
```

Step 4: Start the bench

```
$ bench --site manual.erpnext.com serve --port 8000
```

Open your browser on `http://localhost:8000` to see the site


#### To develop

Disable website caching

1. Open `sites/manual.erpnext.com/site_config.json`
2. Add `"disable_website_cache": 1` to the options
3. Clear the cache: `bench --site manual.erpnext.com clear-cache`

Run `$ bench --site manual.erpnext.com serve --port 8000` again

Edits will appear on the site.

#### Added New Pages?

1. Sync New Pages into Database: `bench --site manual.erpnext.com sync-www`
1. Rebuild Web Page Database: `bench --site manual.erpnext.com sync-www --force`

#### Where to Start?

1. See `frappe-bench/apps/manual_erpnext_com/manual_erpnext_com/www`
1. The home page is `www/index.html`
1. Documentation starts from `www/contents/index.html`
1. `index.txt` holds the table of contents of that folder and will be used to produce a list of pages under that section. Any page you add should be added to its parent folder's `index.txt`. For example, see `www/contents/accounts/index.txt`.
1. `accounts` is a folder. But `https://manual.erpnext.com/contents/accounts` is also a web page. This is handled by having a `index.md` file under `accounts`.
1. All images are to be stored in respective folders under `manual_erpnext_com/public/img`.
1. To link an image in the public folder in the documentation, use `/assets/manual_erpnext_com/img/{path_to_the_image}`. For example: `/assets/manual_erpnext_com/img/accounts/account-settings.png`
1. For any further help, post your question at `https://discuss.erpnext.com` and select the topic category as `Documentation`

#### License

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">ERPNext Manual</span> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.
