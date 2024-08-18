import libtorrent as lt
import time

# 读取种子文件
ses = lt.session()
info = lt.torrent_info('1.torrent')
h = ses.add_torrent({'ti': info, 'save_path': './'})

print('Starting torrent download...')
while not h.is_seed():
    s = h.status()
    print(f'Download rate: {s.download_rate / 1000} kB/s, Progress: {s.progress * 100:.2f}%')
    time.sleep(1)

print('Download complete!')
