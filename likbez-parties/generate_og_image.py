from PIL import Image, ImageDraw, ImageFont


W, H = 1200, 630
BLUE = "#1a3a8f"
BLUE_DARK = "#0b1e55"
PAPER = "#fbfaf7"
YELLOW = "#FFD700"
INK = "#16181d"

FONT_DIR = "/System/Library/Fonts/Supplemental"
ARIAL_BLACK = f"{FONT_DIR}/Arial Black.ttf"
ARIAL_BOLD = f"{FONT_DIR}/Arial Bold.ttf"
ARIAL = f"{FONT_DIR}/Arial.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_text(draw, xy, text, fill, size, path=ARIAL_BLACK):
    draw.text(xy, text, fill=fill, font=font(path, size))


def star(draw, cx, cy, r, color, width):
    up = [(cx, cy - r), (cx + r * 0.88, cy + r * 0.52), (cx - r * 0.88, cy + r * 0.52)]
    down = [(cx, cy + r), (cx - r * 0.88, cy - r * 0.52), (cx + r * 0.88, cy - r * 0.52)]
    draw.line(up + [up[0]], fill=color, width=width, joint="curve")
    draw.line(down + [down[0]], fill=color, width=width, joint="curve")


def main():
    image = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, W, 18), fill=BLUE)
    draw.rectangle((0, H - 18, W, H), fill=BLUE)
    draw.rounded_rectangle((830, 78, 1114, 552), radius=72, fill="#eef3ff")

    draw.rounded_rectangle((902, 138, 1050, 236), radius=8, fill="white")
    draw.rectangle((902, 138, 1050, 154), fill=BLUE)
    draw.rectangle((902, 220, 1050, 236), fill=BLUE)
    star(draw, 976, 187, 18, BLUE, 3)

    draw_text(draw, (76, 78), "Ульпан", BLUE, 34)
    draw_text(draw, (218, 78), ".", YELLOW, 34)
    draw_text(draw, (236, 78), "Политика", BLUE, 34)
    draw_text(draw, (76, 126), "Предвыборный цикл", BLUE, 25, ARIAL_BOLD)

    draw_text(draw, (76, 156), "Партии", BLUE_DARK, 92)
    draw_text(draw, (76, 258), "Израиля:", BLUE_DARK, 92)
    draw_text(draw, (76, 360), "кто есть кто", BLUE_DARK, 82)
    draw_text(draw, (76, 462), "простыми словами", BLUE_DARK, 68)

    draw.rounded_rectangle((78, 552, 328, 594), radius=12, fill=YELLOW)
    draw_text(draw, (104, 558), "Разобраться", INK, 28, ARIAL_BLACK)

    draw_text(draw, (842, 416), "Новости · Интервью", BLUE_DARK, 28, ARIAL_BOLD)
    draw_text(draw, (842, 456), "· Аналитика", BLUE_DARK, 28, ARIAL_BOLD)

    image.save("likbez-parties/og-image.png", "PNG")


if __name__ == "__main__":
    main()
