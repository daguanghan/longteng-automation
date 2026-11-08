#!/usr/bin/env python3
"""官网「方案演示 / Demo」：把一份方案加密后放到 demo/d/<编号>/，客户在 longtengautomation.com/demo/ 输口令在线查看。

  python3 _src/demo_pack.py add <方案清单.json> [--publish]   # 在终端里输入口令（输两次）；直接回车会自动生成一个并显示在终端里
  python3 _src/demo_pack.py list                               # 列出已放上的方案（编号、标题、日期）
  python3 _src/demo_pack.py close <编号> [--publish]            # 关闭：删掉这份方案的加密文件

口令 → PBKDF2-SHA256（310000 次，盐 longteng-demo-v1）→ 48 字节：前 32 字节是 AES-256-GCM 钥匙，后 16 字节是文件夹编号。
网站上只有加密文件：没有口令解不开，文件夹编号也推不出是哪份方案。口令不写进任何文件；登记表只记编号和标题，放在网站仓库之外。
方案清单 JSON：{"title","subtitle","for"(水印上显示，可省),"items":[{"type":"pages|video|html","title","desc","src"}]}；PDF、PPT 用 pages。"""
import base64, getpass, hashlib, io, json, os, re, secrets, shutil, subprocess, sys, tempfile, time
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEMO = os.path.join(REPO, 'demo', 'd')
REG = '/Volumes/HDG-application/广州公司国内申报_2026-10-01/官网方案演示_2026-11-08/登记.json'   # 网站仓库之外，不公开
DOCVIEW = '/Volumes/HDG-application/tools/agent-docview/docview/docview.py'
SALT, ITER = b'longteng-demo-v1', 310000
ALPHA = 'ABCDEFGHJKMNPQRSTUVWXYZ23456789'
norm = lambda s: re.sub(r'[\s\-_]', '', s.upper())


def derive(code):
    b = hashlib.pbkdf2_hmac('sha256', code.encode(), SALT, ITER, 48)
    return b[:32], b[32:48].hex()


def ask_code():
    if os.environ.get('LTDEMO_CODE'):          # 只给自动测试用，不打印
        return norm(os.environ['LTDEMO_CODE'])
    print('口令规则：项目缩写 + 你记得住的 4 位数字（例如 PTC 加 4 位数字）。大小写、短横都不影响。输入时屏幕上不显示字符，是正常的。')
    for n in range(3):
        c = norm(getpass.getpass('请输入口令，然后按回车（直接回车会自动生成一个）：'))
        if not c:
            c = ''.join(secrets.choice(ALPHA) for _ in range(8))
            print(f'\n自动生成的口令：{c[:4]}-{c[4:]}\n（只在这里显示一次，请记下或存进密码管理器；发给客户时可以写成 {c[:4]}-{c[4:]}）\n')
            return c
        if len(c) < 6 or not re.search(r'[A-Z]', c) or not re.search(r'\d', c):
            print('口令至少 6 位，字母和数字都要有（例如项目缩写加 4 位数字），请重新输入。\n'); continue
        if norm(getpass.getpass('再输入一次同样的口令：')) == c:
            return c
        print('两次输入不一样，请重新输入。\n')
    sys.exit('没有设置成功，没有做任何改动。需要时再运行一次。')


def pages(src, out):
    if src.lower().endswith('.pdf'):
        subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', 'quality=80', '-scale-to-x', '1240', '-scale-to-y', '-1', src, os.path.join(out, 'raw')], check=True)
        ims = [Image.open(os.path.join(out, f)) for f in sorted(os.listdir(out)) if f.startswith('raw')]
    else:  # PPT、Word：用 docview（Office 字体）转成逐页图片
        tmp = tempfile.mkdtemp()
        r = subprocess.run(['python3', DOCVIEW, '--out', tmp, src], check=True, capture_output=True, text=True)
        page = r.stdout.strip().splitlines()[-1]; page = page if os.path.isabs(page) else os.path.join(tmp, os.path.basename(page))
        ims = [Image.open(io.BytesIO(base64.b64decode(b))) for b in re.findall(r'src="data:image/(?:png|jpeg|webp);base64,([A-Za-z0-9+/=]+)"', open(page, encoding='utf-8').read())]
        shutil.rmtree(tmp, ignore_errors=True)
    out_b = []
    for im in ims:
        im = im.convert('RGB'); im.thumbnail((1600, 1600)); bio = io.BytesIO(); im.save(bio, 'JPEG', quality=80); out_b.append(bio.getvalue())
    return out_b, ims[0].size if ims else (0, 0)


def seal(aes, data, path):
    nonce = os.urandom(12)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'wb').write(nonce + aes.encrypt(nonce, data, None))


def reg_load():
    return json.load(open(REG, encoding='utf-8')) if os.path.exists(REG) else []


def reg_save(r):
    os.makedirs(os.path.dirname(REG), exist_ok=True)
    json.dump(r, open(REG, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


def publish(msg):
    subprocess.run(['git', 'add', '-A', 'demo'], cwd=REPO, check=True)
    if subprocess.run(['git', 'diff', '--cached', '--quiet'], cwd=REPO).returncode == 0:
        print('没有变化，不用发布。'); return
    subprocess.run(['git', 'commit', '-q', '-m', msg], cwd=REPO, check=True)
    subprocess.run(['git', '-c', 'credential.helper=', '-c', "credential.helper=!gh auth git-credential", 'push', '-q',
                    'https://github.com/daguanghan/longteng-automation.git', 'main'], cwd=REPO, check=True)
    print('已发布到官网（约 1 分钟后生效）：https://longtengautomation.com/demo/')


def add(spec_path, do_publish):
    spec = json.load(open(spec_path, encoding='utf-8'))
    code = ask_code(); key, did = derive(code); aes = AESGCM(key); dst = os.path.join(DEMO, did)
    if os.path.exists(dst):
        sys.exit('这个口令已经用过了，请换一个。')
    items, total = [], 0
    for i, it in enumerate(spec['items']):
        o = {k: it[k] for k in ('type', 'title', 'desc') if k in it}
        if it['type'] == 'pages':
            imgs, (w, h) = pages(it['src'], tempfile.mkdtemp())
            for k, b in enumerate(imgs, 1):
                seal(aes, b, os.path.join(dst, str(i), f'{k:03d}.bin')); total += len(b)
            o.update(count=len(imgs), w=w, h=h)
        elif it['type'] == 'video':
            tmp = os.path.join(tempfile.mkdtemp(), 'v.mp4')
            subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-y', '-i', it['src'], '-vf', 'scale=-2:min(720\\,ih)', '-c:v', 'libx264', '-preset', 'slow', '-crf', '25',
                            '-pix_fmt', 'yuv420p', '-c:a', 'aac', '-b:a', '96k', '-movflags', '+faststart', tmp], check=True)   # 有讲解声音就保留
            b = open(tmp, 'rb').read(); seal(aes, b, os.path.join(dst, str(i), 'a.bin')); total += len(b)
        elif it['type'] == 'html':
            b = open(it['src'], 'rb').read(); seal(aes, b, os.path.join(dst, str(i), 'a.bin')); total += len(b)
        items.append(o); print(f'  {it["title"]}：完成')
    man = {'title': spec['title'], 'subtitle': spec.get('subtitle', ''), 'wm': spec.get('for', ''), 'items': items}
    seal(aes, json.dumps(man, ensure_ascii=False).encode(), os.path.join(dst, 'm.bin'))
    r = reg_load(); r.append({'id': did, 'title': spec['title'], 'subtitle': spec.get('subtitle', ''), 'for': spec.get('for', ''), 'created': time.strftime('%Y-%m-%d %H:%M'), 'mb': round(total / 1e6, 1), 'status': 'open'}); reg_save(r)
    print(f'方案已加密放入官网目录：编号 {did[:8]}…，约 {total / 1e6:.0f} MB')
    if do_publish:
        publish(f'Demo: add one encrypted package')


def close(did, do_publish):
    r = reg_load(); hit = [x for x in r if x['id'].startswith(did)]
    if len(hit) != 1:
        sys.exit('找不到这个编号，或编号不唯一。先运行 list 看一下。')
    shutil.rmtree(os.path.join(DEMO, hit[0]['id']), ignore_errors=True)
    hit[0]['status'] = 'closed'; hit[0]['closed'] = time.strftime('%Y-%m-%d %H:%M'); reg_save(r)
    print(f'已关闭：{hit[0]["title"]}')
    if do_publish:
        publish('Demo: close one package')


if __name__ == '__main__':
    a = sys.argv[1:]; pub = '--publish' in a; a = [x for x in a if x != '--publish']
    if a[:1] == ['add'] and len(a) == 2:
        add(a[1], pub)
    elif a[:1] == ['close'] and len(a) == 2:
        close(a[1], pub)
    elif a[:1] == ['list']:
        for x in reg_load():
            print(f"{x['id'][:8]}  {x['status']:6s}  {x['created']}  {x['title']} {x['subtitle']}  {x.get('for', '')}")
    else:
        print(__doc__)
