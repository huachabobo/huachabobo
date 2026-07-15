#!/usr/bin/env python3
from __future__ import annotations

import math
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


WIDTH = 1200
HEIGHT = 460
DURATION = 12.0
FPS = 6
FRAME_COUNT = int(DURATION * FPS)

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "profile-hero.gif"

PAPER = (255, 247, 232)
MUTED = (169, 170, 169)
PINK = (255, 120, 148)
PINK_SOFT = (255, 157, 176)
MINT = (110, 231, 183)
MINT_SOFT = (168, 241, 209)
GOLD = (245, 199, 104)
GOLD_SOFT = (255, 227, 160)
BLUE = (122, 162, 255)
VOID = (13, 17, 23)

MONO_FONT_PATHS = (
    "/System/Library/Fonts/SFNSMono.ttf",
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
)
CN_FONT_PATHS = (
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/System/Library/Fonts/STHeiti Medium.ttc",
    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
)


def clamp(value: float, low: float = 0.0, high: float = 1.0) -> float:
    return max(low, min(high, value))


def smoothstep(value: float) -> float:
    value = clamp(value)
    return value * value * (3.0 - 2.0 * value)


def mix(a: float, b: float, amount: float) -> float:
    return a + (b - a) * amount


def mix_color(a: tuple[int, int, int], b: tuple[int, int, int], amount: float) -> tuple[int, int, int]:
    return tuple(round(mix(a[index], b[index], amount)) for index in range(3))


def with_alpha(color: tuple[int, int, int], alpha: float | int = 255) -> tuple[int, int, int, int]:
    return (*color, round(clamp(float(alpha), 0.0, 255.0)))


def window_alpha(t: float, start: float, full_start: float, full_end: float, end: float) -> float:
    if t < start or t > end:
        return 0.0
    if t < full_start:
        return smoothstep((t - start) / (full_start - start))
    if t <= full_end:
        return 1.0
    return 1.0 - smoothstep((t - full_end) / (end - full_end))


def cyclic_delta(t: float, event: float, period: float = DURATION) -> float:
    return (t - event + period / 2.0) % period - period / 2.0


def pulse_scale(t: float, event: float, strength: float = 0.28) -> float:
    distance = cyclic_delta(t, event) / 0.24
    return 1.0 + strength * math.exp(-(distance * distance))


def find_font(paths: tuple[str, ...]) -> str:
    for candidate in paths:
        if Path(candidate).exists():
            return candidate
    raise FileNotFoundError(f"No usable font found in: {paths}")


MONO_FONT = find_font(MONO_FONT_PATHS)
CN_FONT = find_font(CN_FONT_PATHS)


@lru_cache(maxsize=None)
def font(size: int, chinese: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(CN_FONT if chinese else MONO_FONT, size=size)


def cubic_points(
    start: tuple[float, float],
    control_a: tuple[float, float],
    control_b: tuple[float, float],
    end: tuple[float, float],
    steps: int = 48,
) -> list[tuple[float, float]]:
    points = []
    for index in range(steps + 1):
        t = index / steps
        inv = 1.0 - t
        x = inv**3 * start[0] + 3 * inv**2 * t * control_a[0] + 3 * inv * t**2 * control_b[0] + t**3 * end[0]
        y = inv**3 * start[1] + 3 * inv**2 * t * control_a[1] + 3 * inv * t**2 * control_b[1] + t**3 * end[1]
        points.append((x, y))
    return points


def joined_curve(segments: list[tuple[tuple[float, float], ...]]) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for segment in segments:
        sampled = cubic_points(*segment)
        points.extend(sampled if not points else sampled[1:])
    return points


LEFT_ROUTE = joined_curve(
    [
        ((70, 220), (128, 220), (151, 155), (220, 155)),
        ((220, 155), (289, 155), (300, 258), (365, 248)),
        ((365, 248), (424, 239), (463, 188), (535, 212)),
    ]
)
RIGHT_ROUTE = joined_curve(
    [
        ((665, 212), (731, 166), (757, 137), (820, 160)),
        ((820, 160), (886, 184), (899, 272), (965, 248)),
        ((965, 248), (1029, 224), (1057, 161), (1135, 212)),
    ]
)


def color_at(stops: list[tuple[float, tuple[int, int, int]]], position: float) -> tuple[int, int, int]:
    for index in range(len(stops) - 1):
        left_pos, left_color = stops[index]
        right_pos, right_color = stops[index + 1]
        if position <= right_pos:
            local = (position - left_pos) / (right_pos - left_pos)
            return mix_color(left_color, right_color, clamp(local))
    return stops[-1][1]


def point_on_route(points: list[tuple[float, float]], progress: float) -> tuple[float, float]:
    cursor = clamp(progress) * (len(points) - 1)
    index = min(int(cursor), len(points) - 2)
    local = cursor - index
    return (mix(points[index][0], points[index + 1][0], local), mix(points[index][1], points[index + 1][1], local))


def draw_progress_route(
    draw: ImageDraw.ImageDraw,
    points: list[tuple[float, float]],
    progress: float,
    stops: list[tuple[float, tuple[int, int, int]]],
) -> None:
    limit = clamp(progress) * (len(points) - 1)
    whole = int(limit)
    for index in range(min(whole, len(points) - 1)):
        draw.line((points[index], points[index + 1]), fill=with_alpha(color_at(stops, index / (len(points) - 1))), width=4)
    if whole < len(points) - 1 and limit > whole:
        end = point_on_route(points, progress)
        draw.line((points[whole], end), fill=with_alpha(color_at(stops, progress)), width=4)


def draw_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    value: str,
    size: int,
    color: tuple[int, int, int],
    alpha: float | int = 255,
    anchor: str = "la",
    chinese: bool = False,
    stroke: int = 0,
) -> None:
    draw.text(
        xy,
        value,
        font=font(size, chinese),
        fill=with_alpha(color, alpha),
        anchor=anchor,
        stroke_width=stroke,
        stroke_fill=with_alpha(color, alpha),
    )


def make_background() -> Image.Image:
    image = Image.new("RGBA", (WIDTH, HEIGHT), (*VOID, 255))
    gradient = Image.new("RGBA", (WIDTH, HEIGHT))
    gradient_draw = ImageDraw.Draw(gradient)
    for y in range(HEIGHT):
        vertical = y / (HEIGHT - 1)
        left = mix_color((16, 19, 26), (20, 18, 23), vertical)
        right = mix_color((17, 26, 24), (16, 22, 21), vertical)
        for x in range(0, WIDTH, 8):
            color = mix_color(left, right, x / (WIDTH - 1))
            gradient_draw.rectangle((x, y, min(x + 7, WIDTH), y), fill=(*color, 255))

    mask = Image.new("L", (WIDTH, HEIGHT), 0)
    ImageDraw.Draw(mask).rounded_rectangle((8, 8, 1192, 452), radius=34, fill=255)
    image.paste(gradient, (0, 0), mask)

    static = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(static)
    draw.rounded_rectangle((8, 8, 1192, 452), radius=34, outline=with_alpha(PAPER, 58), width=2)
    for x in range(28, 1177, 28):
        draw.line((x, 24, x, 436), fill=with_alpha(PAPER, 11), width=1)
    for y in range(28, 437, 28):
        draw.line((24, y, 1176, y), fill=with_alpha(PAPER, 11), width=1)

    draw.rounded_rectangle((42, 38, 308, 72), radius=17, fill=with_alpha(PAPER, 20), outline=with_alpha(PAPER, 36), width=1)
    draw.ellipse((58, 50, 68, 60), fill=with_alpha(PINK))
    draw_text(draw, (80, 55), "DUAL-CORE BOOT / HUACHABOBO", 13, PAPER, anchor="lm", stroke=1)
    draw_text(draw, (1152, 55), "12.0 SEC LOOP", 12, MUTED, anchor="rm", stroke=1)

    draw.rounded_rectangle((458, 37, 742, 73), radius=18, fill=(9, 11, 15, 255), outline=with_alpha(PAPER, 40), width=1)
    draw_text(draw, (56, 104), "LECIA / GOVERNED CONTROL PLANE", 13, PINK_SOFT, anchor="lm", stroke=1)
    draw_text(draw, (1144, 104), "CODELIFE / PUBLIC LIFE LOOP", 13, MINT, anchor="rm", stroke=1)

    draw.line(LEFT_ROUTE, fill=with_alpha(PAPER, 24), width=18, joint="curve")
    draw.line(RIGHT_ROUTE, fill=with_alpha(PAPER, 24), width=18, joint="curve")

    labels = [
        ((100, 253), "OPERATOR"),
        ((220, 132), "POLICY"),
        ((365, 282), "RUNTIME"),
        ((490, 177), "EVIDENCE"),
        ((710, 219), "GENOME"),
        ((820, 136), "LIFEVM"),
        ((965, 282), "ENERGY"),
        ((1095, 164), "LINEAGE"),
    ]
    for position, value in labels:
        draw_text(draw, position, value, 12, PAPER, anchor="mm", stroke=1)

    draw_text(draw, (600, 309), "HUACHA CORE", 12, MUTED, anchor="mm", stroke=1)
    draw_text(draw, (42, 425), "LECIA AGENTOS", 12, MUTED, anchor="lm", stroke=1)
    draw_text(draw, (1158, 425), "CODELIFE LAB", 12, MUTED, anchor="rm", stroke=1)
    return Image.alpha_composite(image, static)


BACKGROUND = make_background()


def draw_diamond(draw: ImageDraw.ImageDraw, center: tuple[float, float], radius: float, color: tuple[int, int, int], alpha: int) -> None:
    x, y = center
    points = ((x, y - radius), (x + radius * 0.42, y - radius * 0.42), (x + radius, y), (x + radius * 0.42, y + radius * 0.42), (x, y + radius), (x - radius * 0.42, y + radius * 0.42), (x - radius, y), (x - radius * 0.42, y - radius * 0.42))
    draw.polygon(points, fill=with_alpha(color, alpha))


def draw_node(draw: ImageDraw.ImageDraw, center: tuple[float, float], color: tuple[int, int, int], scale: float) -> None:
    x, y = center
    outer = 16 * scale
    halo = 23 * scale
    draw.ellipse((x - halo, y - halo, x + halo, y + halo), fill=with_alpha(color, 22))
    draw.ellipse((x - outer, y - outer, x + outer, y + outer), fill=with_alpha(color))
    draw.ellipse((x - 6, y - 6, x + 6, y + 6), fill=with_alpha(PAPER))


def draw_petal(draw: ImageDraw.ImageDraw, angle: float, color: tuple[int, int, int], alpha: int, breathe: float) -> None:
    direction = (math.sin(angle), -math.cos(angle))
    perpendicular = (math.cos(angle), math.sin(angle))
    center = (600 + direction[0] * 40 * breathe, 212 + direction[1] * 40 * breathe)
    half_length = 14 * breathe
    half_width = 11 * breathe
    top = (center[0] + direction[0] * half_length, center[1] + direction[1] * half_length)
    bottom = (center[0] - direction[0] * half_length, center[1] - direction[1] * half_length)
    polygon = [
        (top[0] + perpendicular[0] * half_width, top[1] + perpendicular[1] * half_width),
        (top[0] - perpendicular[0] * half_width, top[1] - perpendicular[1] * half_width),
        (bottom[0] - perpendicular[0] * half_width, bottom[1] - perpendicular[1] * half_width),
        (bottom[0] + perpendicular[0] * half_width, bottom[1] + perpendicular[1] * half_width),
    ]
    draw.polygon(polygon, fill=with_alpha(color, alpha))
    for end in (top, bottom):
        draw.ellipse((end[0] - half_width, end[1] - half_width, end[0] + half_width, end[1] + half_width), fill=with_alpha(color, alpha))


def draw_packet(draw: ImageDraw.ImageDraw, position: tuple[float, float], color: tuple[int, int, int], alpha: float) -> None:
    if alpha <= 0:
        return
    x, y = position
    draw.ellipse((x - 13, y - 13, x + 13, y + 13), fill=with_alpha(color, 24 * alpha))
    draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=with_alpha(color, 72 * alpha))
    draw.ellipse((x - 4, y - 4, x + 4, y + 4), fill=with_alpha(PAPER, 255 * alpha))


def render_frame(t: float) -> Image.Image:
    frame = BACKGROUND.copy()
    layer = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)

    scan_phase = (t % 6.0) / 6.0
    scan_y = -8 + scan_phase * 476
    scan_alpha = int(95 * math.sin(math.pi * scan_phase) ** 1.5)
    for x in range(24, 1176, 8):
        edge = abs((x - 600) / 576)
        color = mix_color(MINT, PINK, x / WIDTH)
        draw.rectangle((x, scan_y, x + 8, scan_y + 2), fill=with_alpha(color, scan_alpha * (1.0 - edge * 0.65)))

    left_progress = smoothstep((t - 0.3) / 3.4)
    right_progress = smoothstep((t - 3.0) / 3.7)
    draw_progress_route(draw, LEFT_ROUTE, left_progress, [(0.0, PINK), (0.55, GOLD), (1.0, PAPER)])
    draw_progress_route(draw, RIGHT_ROUTE, right_progress, [(0.0, PAPER), (0.45, MINT), (1.0, BLUE)])

    left_nodes = [((100, 218), PINK, 1.25), ((220, 155), PINK_SOFT, 2.15), ((365, 248), GOLD, 3.05), ((490, 200), GOLD_SOFT, 3.95)]
    right_nodes = [((710, 185), MINT_SOFT, 3.9), ((820, 160), MINT, 4.8), ((965, 248), (106, 207, 180), 5.7), ((1095, 187), BLUE, 6.6)]
    for center, color, event in left_nodes + right_nodes:
        draw_node(draw, center, color, pulse_scale(t, event))

    left_packet_alpha = window_alpha(t, 0.8, 1.1, 3.7, 4.2)
    right_packet_alpha = window_alpha(t, 3.8, 4.1, 6.9, 7.5)
    draw_packet(draw, point_on_route(LEFT_ROUTE, clamp((t - 1.0) / 3.1)), PINK, left_packet_alpha)
    draw_packet(draw, point_on_route(RIGHT_ROUTE, clamp((t - 4.0) / 3.1)), MINT, right_packet_alpha)

    breathe = 0.98 + 0.045 * math.sin(2 * math.pi * t / 3.2)
    draw.ellipse((518, 130, 682, 294), outline=with_alpha(PAPER, 24), width=1)
    orbit_rotation = 360 * t / 8.0
    for dash in range(24):
        start = orbit_rotation + dash * 15
        draw.arc((532, 144, 668, 280), start=start, end=start + 4.5, fill=with_alpha(PAPER, 74), width=1)

    orbit_angle = 2 * math.pi * t / 7.0
    for offset, color in ((0.0, PINK), (math.pi, MINT)):
        x = 600 + math.sin(orbit_angle + offset) * 70
        y = 212 - math.cos(orbit_angle + offset) * 70
        draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill=with_alpha(color))

    petal_colors = (PINK, GOLD, MINT, BLUE, GOLD, PINK_SOFT)
    rotor = 2 * math.pi * t / 10.0
    for index, color in enumerate(petal_colors):
        wave = 0.58 + 0.42 * (0.5 + 0.5 * math.sin(2 * math.pi * t / 3.6 - index * math.pi / 3))
        draw_petal(draw, rotor + index * math.pi / 3, color, int(255 * wave), breathe)

    core_radius = 31 * breathe
    draw.ellipse((600 - core_radius - 8, 212 - core_radius - 8, 600 + core_radius + 8, 212 + core_radius + 8), fill=with_alpha(GOLD, 25))
    draw.ellipse((600 - core_radius, 212 - core_radius, 600 + core_radius, 212 + core_radius), fill=with_alpha(GOLD))
    draw.ellipse((576, 188, 624, 236), fill=(21, 20, 25, 255))
    draw_text(draw, (600, 213), "茶", 22, PAPER, anchor="mm", chinese=True, stroke=1)

    spark_a_y = 124 - 8 * math.sin(2 * math.pi * t / 4.8)
    spark_b_y = 107 - 8 * math.sin(2 * math.pi * (t - 1.1) / 5.6)
    draw_diamond(draw, (335, spark_a_y), 19, PINK, 150)
    draw_diamond(draw, (888, spark_b_y), 17, MINT, 150)
    draw.ellipse((1051, 322, 1059, 330), fill=with_alpha(BLUE, 155))
    draw.ellipse((147, 324, 153, 330), fill=with_alpha(GOLD, 170))

    statuses = [
        ("BOOTING RUNTIME", PINK, window_alpha(t, 0.05, 0.4, 2.2, 2.6)),
        ("VERIFYING POLICY", GOLD, window_alpha(t, 2.25, 2.65, 4.45, 4.9)),
        ("SPAWNING LINEAGE", MINT, window_alpha(t, 4.55, 5.0, 6.95, 7.4)),
        ("SYSTEM ONLINE", MINT, window_alpha(t, 7.05, 7.55, 11.15, 11.7)),
    ]
    for label, color, alpha in statuses:
        if alpha <= 0:
            continue
        draw.ellipse((475, 50, 485, 60), fill=with_alpha(color, 255 * alpha))
        draw_text(draw, (600, 56), label, 13, PAPER, 255 * alpha, anchor="mm", stroke=1)

    final_alpha = window_alpha(t, 6.7, 7.35, 11.2, 11.75)
    if final_alpha > 0:
        draw_text(draw, (600, 356), "SYSTEMS THAT CAN EXPLAIN THEMSELVES", 29, PAPER, 255 * final_alpha, anchor="mm", stroke=1)
        draw_text(draw, (600, 397), "让系统运行，也让系统解释自己。", 18, (200, 202, 200), 255 * final_alpha, anchor="mm", chinese=True, stroke=1)

    return Image.alpha_composite(frame, layer).convert("RGB")


def main() -> None:
    frames = [render_frame(index / FPS) for index in range(FRAME_COUNT)]
    palette = render_frame(8.0).quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    paletted = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    frame_durations = [170 if index % 3 != 2 else 160 for index in range(FRAME_COUNT)]
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    paletted[0].save(
        OUTPUT,
        save_all=True,
        append_images=paletted[1:],
        duration=frame_durations,
        loop=0,
        optimize=False,
        disposal=2,
    )
    print(f"wrote {OUTPUT} ({OUTPUT.stat().st_size / 1024 / 1024:.2f} MiB, {FRAME_COUNT} frames)")


if __name__ == "__main__":
    main()
