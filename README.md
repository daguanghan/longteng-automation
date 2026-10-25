# longtengautomation.com

Trilingual (English · Tiếng Việt · 中文) export website for Guangzhou Longteng Automation Equipment Co., Ltd., aimed at factories in Vietnam.

- Edit text in `_src/content.py`, layout in `_src/build.py`, styles in `assets/css/site.css`.
- Rebuild: `python3 _src/build.py` (writes the 18 pages and single-file previews in `preview/`, which are not committed).
- Draft mode: `DRAFT = True` in `_src/build.py` adds `noindex` and a draft banner; `robots.txt` blocks crawlers. Switch both off at launch.
- Hosted on GitHub Pages with the custom domain in `CNAME`.
