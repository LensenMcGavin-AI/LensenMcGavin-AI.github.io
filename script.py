try:
    from PIL import Image
    from collections import Counter
    img = Image.open('images/lm-ai-logo.png').convert('RGBA')
    pixels = list(img.getdata())
    colors = Counter([p for p in pixels if p[3] > 0]) # Ignore transparent
    for c, count in colors.most_common(10):
        print(f'#{c[0]:02x}{c[1]:02x}{c[2]:02x}', count)
except Exception as e:
    print('Error:', e)
