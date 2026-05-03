from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
CSS = (ROOT / "css" / "style.css").read_text(encoding="utf-8")


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing {label}: {needle}")


def forbid(text: str, needle: str, label: str) -> None:
    if needle in text:
        raise AssertionError(f"unexpected {label}: {needle}")


require(HTML, "西西Claire", "site name")
require(HTML, "AI产品 / vibe coding / marketing", "subtitle")
require(HTML, 'href="css/style.css?v=20260503-1"', "css version")
require(HTML, 'src="js/main.js?v=20260503-1"', "js version")
require(HTML, 'src="public/avatar.svg?v=20260503-1"', "avatar asset")

for anchor in [
    "featured-projects",
    "ai-insights",
    "ai-gateway",
    "ai-recharge",
    "contact",
]:
    require(HTML, f'id="{anchor}"', f"anchor {anchor}")

for text in [
    "精选项目",
    "AI见闻",
    "AI高质量中转",
    "AI代充",
    "Claude 代充",
    "ChatGPT 代充",
    "西西碎碎念",
    "CindyW2020",
    "成都",
]:
    require(HTML, text, text)

for href in [
    'href="https://blog.aistar.cool/projects"',
    'href="https://blog.aistar.cool/blogs"',
    'href="https://code.aistar.cool"',
    'href="https://store.reshub.vip/"',
    'target="_blank"',
    'rel="noopener"',
]:
    require(HTML, href, href)

for klass in [
    "meta-item--xiaohongshu",
    "meta-item--wechat",
    "entry-card",
]:
    require(HTML + CSS, klass, klass)

for removed in [
    "AI精选项目",
    "curated-ai-projects",
    "detail-stack",
    "detail-panel",
    "个人品牌主页",
    "产品包装",
]:
    forbid(HTML, removed, removed)

if HTML.count('class="entry-card"') != 4:
    raise AssertionError("expected exactly 4 entry cards")

if HTML.count('class="entry-arrow"') != 4:
    raise AssertionError("expected exactly 4 entry arrows")

print("PASS")
